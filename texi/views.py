#-*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.template.response import TemplateResponse
from django.template import RequestContext 
from django.contrib.sites.models import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.utils.http import base36_to_int, is_safe_url
from django.utils import simplejson
from django.db import connection, transaction

from texi.models import Notification, Driver, Driver_bargin, Driver_exam, Car
from texi.forms import AuthenticationForm, NotificationForm, DriverForm, CarForm


@login_required
def index(request):

	s = 'hello world!'

	return render_to_response('index.html', locals())

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_view(request, template_name='registration/login.html',
				redirect_field_name=REDIRECT_FIELD_NAME,
				authentication_form=AuthenticationForm,
				current_app=None, extra_context=None):
	"""
		Displays the login form and handles the login action.
	"""
	redirect_to = request.REQUEST.get(redirect_field_name, '')

	if request.method == "POST":
		form = authentication_form(data=request.POST)

		if form.is_valid():

			if not is_safe_url(url=redirect_to, host=request.get_host()):
 				redirect_to = '/'

			user = form.get_user()
			username = user.username
			password = user.password

			auth_login(request, user)

			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()
			return HttpResponseRedirect(redirect_to)
		else:
			messages.error(request, '用户名或密码错误！(如忘记密码, 请联系管理员)')
	else:
		form = authentication_form(request)

	request.session.set_test_cookie()

	current_site = get_current_site(request)

	context = {
			'form': form,
			redirect_field_name: redirect_to,
			'site': current_site,
			'site_name': current_site.name,
	}
	if extra_context is not None:
		context.update(extra_context)
	return TemplateResponse(request, template_name, context, current_app=current_app)

def logout_view(request):
	messages.success(request, '退出成功.')
	auth_logout(request)
	return redirect('/accounts/login')

@login_required
def profile_view(request):
	if request.method == 'POST':
		username = request.POST.get('username', '')
		name = request.POST.get('name', '')

		errors = []
		user = User.objects.get(username=username)

		used_name = user.first_name

		password = request.POST.get('password', '')
		confirm_password = request.POST.get('confirm_password', '')

		if used_name != name:
			user.first_name = name
			user.save()
			messages.success(request, '用户信息更新成功.')

		if password != '' and password == confirm_password:
			messages.success(request, '密码更新成功.')
			user.set_password(password)
			user.save()
		elif password != confirm_password:
			messages.error(request, '两次密码不一致.')
		else:
			pass

		return HttpResponseRedirect('/accounts/profile/')
	return render_to_response('profile.html', {'request': request}, context_instance=RequestContext(request))

def display_meta(request):
	values = request.META.items()
	values.sort()

	html = []

	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def test(request):
	return render_to_response('test.html')



@login_required
def notificationedit(request):
	notification = Notification.objects.get(id=1)

	if request.method == 'POST':
		form = NotificationForm(request.POST, instance=notification)
		if form.is_valid():
			notification = form.save()
			messages.success(request, '修改成功.')
			return HttpResponseRedirect('/office/notification')
	return render_to_response('notification.html', {'form':NotificationForm(instance=notification), 'request':request}, context_instance=RequestContext(request))


@login_required
def driver_list(request, types=''):

	if types == 'all':
		drivers = Driver.objects.filter(valid=1).order_by('-id')
	if types == 'daipin':
		drivers = Driver.objects.filter(valid=1, jiasyzt='待聘').order_by('-id')
	if types == 'jiepin':
		drivers = Driver.objects.filter(valid=1, jiasyzt='解聘').order_by('-id')


	return render_to_response('driver_list.html', locals())

@login_required
def driver_single(request, id=''):
	driver = Driver.objects.get(id=int(id))
	driver_bargins = driver.driver_bargin_set.filter(valid=1).order_by('-id')
	driver_exams = driver.driver_exam_set.filter(valid=1).order_by('-id')
	return render_to_response('driver_single.html', locals())

@login_required
@permission_required('texi.add_driver')
def driver_add(request):
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if form.is_valid():
			driver = form.save()
			return HttpResponseRedirect('/driver/single/'+str(driver.id))
	return render_to_response('driver_edit.html', {'form':DriverForm(), 'request':request}, context_instance=RequestContext(request))

@login_required
@permission_required('texi.change_driver')
def driver_edit(request, id=''):
	driver = get_object_or_404(Driver, pk=int(id))
	if request.method == 'POST':
		form = DriverForm(request.POST, instance=driver)
		if form.is_valid():
			driver = form.save()
			return HttpResponseRedirect('/driver/single/'+id)
	return render_to_response('driver_edit.html', {'form':DriverForm(instance=driver), 'request':request}, context_instance=RequestContext(request))

@login_required
@transaction.commit_on_success
@permission_required('texi.delete_driver')
def deletedriver(request, id=''):
	cur = connection.cursor()
	sql = 'update texi_driver set valid=0 where id=%s' % id
	cur.execute(sql)
	return HttpResponseRedirect('/driver/list/all')

@login_required
@transaction.commit_on_success
@permission_required('texi.delete_driver_exam')
def delete_driver_exam(request, id=''):
	cur = connection.cursor()
	sql = 'update texi_driver_exam set valid=0 where id=%s' % id
	cur.execute(sql)
	return HttpResponse('done')


@login_required
def car_list(request):
	cars = Car.objects.filter(valid=1).order_by('cheph')

	return render_to_response('car_list.html', locals())

@login_required
def car_single(request, id=''):
	car = Car.objects.get(id=int(id))

	return render_to_response('car_single.html', locals())

@login_required
@permission_required('texi.add_car')
def car_add(request):
	if request.method == 'POST':
		form = CarForm(request.POST)
		if form.is_valid():
			car = form.save()
			return HttpResponseRedirect('/car/single/'+str(car.id))
	return render_to_response('car_edit.html', {'form':CarForm(), 'request':request}, context_instance=RequestContext(request))

@login_required
@permission_required('texi.change_car')
def car_edit(request, id=''):
	car = get_object_or_404(Car, pk=int(id))
	if request.method == 'POST':
		form = CarForm(request.POST, instance=car)
		if form.is_valid():
			car = form.save()
			return HttpResponseRedirect('/car/single/'+id)
	return render_to_response('car_edit.html', {'form':CarForm(instance=car), 'request':request}, context_instance=RequestContext(request))



@login_required
@transaction.commit_on_success
@permission_required('texi.delete_car')
def deletecar(request, id=''):
	cur = connection.cursor()
	sql = 'update texi_car set valid=0 where id=%s' % id
	cur.execute(sql)
	return HttpResponseRedirect('/car/list')

@login_required
def del_car_driver(request, carid, driverid):
	car = Car.objects.get(id=int(carid))
	driver = Driver.objects.get(id=int(driverid))

	car.driver_set.remove(driver)

	return HttpResponse('done')



