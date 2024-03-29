#-*- coding: utf-8 -*-

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext, ugettext_lazy as _

from texi.models import Notification, Driver, Car

class AuthenticationForm(forms.Form):
	"""
	Base class for authenticating users. Extend this to get a form that accepts
	username/password logins.
	"""
	username = forms.CharField(label=_("Username"), max_length=30)
	password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

	error_messages = {
		'invalid_login': _("Please enter a correct username and password. "
								"Note that both fields are case-sensitive."),
		'no_cookies': _("Your Web browser doesn't appear to have cookies "
								"enabled. Cookies are required for logging in."),
		'inactive': _("This account is inactive."),
	}

	def __init__(self, request=None, *args, **kwargs):
		"""
		If request is passed in, the form will validate that cookies are
		enabled. Note that the request (a HttpRequest object) must have set a
		cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
		running this validation.
		"""
		self.request = request
		self.user_cache = None
		super(AuthenticationForm, self).__init__(*args, **kwargs)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:

			self.user_cache = authenticate(username=username, password=password)

			if self.user_cache is None:
				raise forms.ValidationError(self.error_messages['invalid_login'])
			elif not self.user_cache.is_active:
				raise forms.ValidationError(self.error_messages['inactive'])
		self.check_for_test_cookie()
		return self.cleaned_data

	def check_for_test_cookie(self):
		if self.request and not self.request.session.test_cookie_worked():
			raise forms.ValidationError(self.error_messages['no_cookies'])

	def get_user_id(self):
		if self.user_cache:
			return self.user_cache.id
		return None

	def get_user(self):
		return self.user_cache

class NotificationForm(forms.ModelForm):
	class Meta:
		model = Notification


class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver

		exclude = ('car', 'zhaop', 'shenfzsm', 'jiaszsm', 'fuwzgzsm', 'valid', )
		
class CarForm(forms.ModelForm):
	class Meta:
		model = Car