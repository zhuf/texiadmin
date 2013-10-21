#!-*- coding: utf-8 -*-

from django.db import models

class Notification(models.Model):
	jingyxkz = models.IntegerField(u'经营许可证')
	yingyzz = models.IntegerField(u'营业执照')
	jiasyjsz = models.IntegerField(u'驾驶员驾驶证')
	erbrq = models.IntegerField(u'二保日期')
	fuwzgz = models.IntegerField(u'服务资格证')
	baotrq = models.IntegerField(u'报停日期')
	jiasyht = models.IntegerField(u'驾驶员合同')
	shuiwdjz = models.IntegerField(u'税务登记证')
	jingyjzrq = models.IntegerField(u'经营截止日期')
	baoxrq = models.IntegerField(u'保险日期')
	jingyht = models.IntegerField(u'经营合同')
	shenyrq = models.IntegerField(u'审验日期')
	jijqns = models.IntegerField(u'计价器年审')
	jiasysb = models.IntegerField(u'驾驶员社保')

	class Meta:
		verbose_name = u'时间提醒设置'

class Car(models.Model):

	JINGYLB_CHOICES = (
		(u'一类承包', u'一类承包'),
		(u'二类承包', u'二类承包'),
		(u'三类承包', u'三类承包'),
		(u'自主经营', u'自主经营'),
		(u'挂靠', u'挂靠'),
		)

	CHELXH_CHOICES = (
		(u'普桑', u'普桑'),
		(u'捷达', u'捷达'),
		(u'捷达汽油', u'捷达汽油'),
		(u'2000型', u'2000型'),
		(u'3000型', u'3000型'),
		(u'现代伊兰特', u'现代伊兰特'),
		(u'帕萨特', u'帕萨特'),
		(u'富美来', u'富美来'),
		(u'志俊', u'志俊'),
		(u'广本雅阁', u'广本雅阁'),
		(u'奇瑞', u'奇瑞'),
		(u'起亚福瑞迪', u'起亚福瑞迪'),
		(u'其他', u'其他')
		)

	CHESYS_CHOICES = (
		(u'蓝色', u'蓝色'),
		(u'上白下蓝', u'上白下蓝'),
		(u'上黄下灰', u'上黄下灰'),
		(u'其他', u'其他')
		)

	RANYLB_CHOICES = (
		(u'汽油', u'汽油'),
		(u'柴油', u'柴油'),
		(u'其他', u'其他')
		)

	YUNYZT_CHOICES = (
		(u'营运', u'营运'),
		(u'报停', u'报停')
		)

	chezxm = models.CharField(u'车主姓名/单位', max_length=100, blank=True)
	dianh = models.CharField(u'电话', max_length=32, blank=True, null=True)
	shenfzh = models.CharField(u'身份证号', max_length=32, blank=True, null=True)
	diz = models.CharField(u'地址', max_length=100, blank=True, null=True)
	chengbr = models.CharField(u'承包人', max_length=32, blank=True, null=True)
	chengbrdh = models.CharField(u'承包人电话', max_length=32, blank=True, null=True)
	hegz = models.CharField(u'合格证', max_length=32, blank=True, null=True)
	jiandrq = models.DateField(u'建档日期', auto_now=True, blank=True, null=True)
	cheph = models.CharField(u'车牌号', max_length=20)
	fazrq = models.DateField(u'发证日期', blank=True, null=True)
	jingylb = models.CharField(u'经营类别', max_length=30, choices=JINGYLB_CHOICES, blank=True, null=True)
	chelxh = models.CharField(u'车辆型号', max_length=30, choices=CHELXH_CHOICES, blank=True, null=True)
	chesys = models.CharField(u'车身颜色', max_length=30, choices=CHESYS_CHOICES, blank=True, null=True)
	ranylb = models.CharField(u'燃油类别', max_length=30, choices=RANYLB_CHOICES, blank=True, null=True)
	fadjh = models.CharField(u'发动机号', max_length=32, blank=True, null=True)
	chejh = models.CharField(u'车架号', max_length=32, blank=True, null=True)
	yingyzh = models.CharField(u'营运证号', max_length=32, blank=True, null=True)
	yingyzfzrq = models.DateField(u'营运证发证日期', blank=True, null=True)
	jijqh = models.CharField(u'计价器号', max_length=32, blank=True, null=True)
	zuow = models.CharField(u'吨(座)位', max_length=20, blank=True, null=True)
	chelfjfhm = models.CharField(u'车辆附加费号码', max_length=32, blank=True, null=True)
	jidcdjzsh = models.CharField(u'机动车登记证书号', max_length=32, blank=True, null=True)
	jingyxkzhm = models.CharField(u'经营许可证号码', max_length=32, blank=True, null=True)
	jingyxkzyxq = models.DateField(u'经营许可证有效期', blank=True, null=True)
	shuiwdjzhm = models.CharField(u'税务登记证号码', max_length=32, blank=True, null=True)
	shuiwdjzyxq = models.DateField(u'税务登记证有效期', blank=True, null=True)
	yingyzzhm = models.CharField(u'营业执照号码', max_length=32, blank=True, null=True)
	yingyzzyxq = models.DateField(u'营业执照有效期', blank=True, null=True)
	cheljsdah = models.CharField(u'车辆技术档案号', max_length=32, blank=True, null=True)
	goucfp = models.CharField(u'购车发票', max_length=100, blank=True, null=True)
	jingyjzrq = models.DateField(u'经营截止日期', blank=True, null=True)
	gpszjsj = models.DateField(u'GPS装机时间', auto_now=True, blank=True, null=True)
	gpshm = models.CharField(u'gps号码', max_length=32, blank=True, null=True)
	gpsmm = models.CharField(u'gps密码', max_length=32, blank=True, null=True)
	shiycfp = models.CharField(u'市有偿发票', max_length=32, blank=True, null=True)
	shikprq = models.DateField(u'市开票日期', blank=True, null=True)
	shiycsyf = models.CharField(u'市有偿使用费', max_length=32, blank=True, null=True)
	quycfp = models.CharField(u'区有偿发票', max_length=32, blank=True, null=True)
	qukprq = models.DateField(u'区开票日期', blank=True, null=True)
	quycsyf = models.CharField(u'区有偿使用费', max_length=32, blank=True, null=True)
	yunyzt = models.CharField(u'运营状态', max_length=32, choices=YUNYZT_CHOICES, blank=True, null=True)

#	drivers = models.ManyToManyField(Driver, blank=True)


	beiz = models.CharField(u'备注', max_length=100, blank=True, null=True)

	zhaop = models.ImageField(u'照片', upload_to='car/zhaopian', blank=True, null=True)
	xingszsm = models.ImageField(u'行驶证扫描', upload_to='car/xingshizheng', blank=True, null=True)
	yingyzsm = models.ImageField(u'营运证扫描', upload_to='car/yingyunzheng', blank=True, null=True)

	valid = models.IntegerField(u'是否有效', default='1', editable=False)

	def delete(self, *args, **kwargs):
		storage, path = self.zhaop.storage, self.zhaop.path

		super(Car, self).delete(*args, **kwargs)
		storage.delete(path)

		storage, path = self.xingszsm.storage, self.xingszsm.path

		super(Car, self).delete(*args, **kwargs)
		storage.delete(path)

		storage, path = self.yingyzsm.storage, self.yingyzsm.path

		super(Car, self).delete(*args, **kwargs)
		storage.delete(path)

	def __unicode__(self):
		return self.cheph

	class Meta:
		verbose_name = u'车辆信息'


class Driver(models.Model):

	GENDER_CHOICES = (
			(u'男', u'男'),
			(u'女', u'女'),
		)

	EDU_CHOICES = (
			(u'无', u'无'),
			(u'小学', u'小学'),
			(u'初中', u'初中'),
			(u'高中', u'高中'),
			(u'大专', u'大专'),
			(u'本科', u'本科'),
		)

	STATE_CHOICES = (
			(u'在岗', u'在岗'),
			(u'待聘', u'待聘'),
			(u'解聘', u'解聘'),
			(u'寄存', u'寄存'),
			(u'转大众', u'转大众'),
			(u'转泽圆', u'转泽圆'),
			(u'转泽兴', u'转泽兴'),
			(u'转兴安', u'转兴安'),
			(u'转阳光', u'转阳光'),
			(u'转现代', u'转现代'),
			(u'其它', u'其它'),
		)

	POLICY_CHOICES = (
			(u'清', u'清'),
			(u'党员', u'党员'),
		)

	jiasyxm = models.CharField(u'驾驶员姓名', max_length=100)
	xingb = models.CharField(u'性别', choices=GENDER_CHOICES, max_length=30, blank=True, null=True)
	wenhcd = models.CharField(u'文化程度', choices=EDU_CHOICES, max_length=30, blank=True, null=True)
	jiasyzt = models.CharField(u'驾驶员状态', choices=STATE_CHOICES, max_length=30, blank=True, null=True)
	shenfzh = models.CharField(u'身份证号', max_length=32, blank=True, null=True)
	jiasydh = models.CharField(u'驾驶员电话', max_length=32, blank=True, null=True)
	hujszd = models.CharField(u'户籍所在地', max_length=100, blank=True, null=True)
	jig = models.CharField(u'籍贯', max_length=100, blank=True, null=True)
	jiaszh = models.CharField(u'驾驶证号', max_length=32, blank=True, null=True)
	zhunj = models.CharField(u'准驾', max_length=32, blank=True, null=True)
	chuclz = models.DateField(u'初次领证', blank=True, null=True)
	pinyrq = models.DateField(u'聘用日期', blank=True, null=True)
	shenyrq = models.DateField(u'审验日期', blank=True, null=True)
	jiaszyxq = models.DateField(u'驾驶证有效期', blank=True, null=True)
	xinykh = models.CharField(u'信用卡号', max_length=32, blank=True, null=True)
	fuwzgzh = models.CharField(u'服务资格证号', max_length=32, blank=True, null=True)
	zhengzmm = models.CharField(u'政治面貌', choices=POLICY_CHOICES, max_length=30, blank=True, null=True)
	zanzh = models.CharField(u'暂住号', max_length=32, blank=True, null=True)
	zanzyxqz = models.DateField(u'暂住有效期止', blank=True, null=True)
	zanzd = models.CharField(u'暂住地', max_length=100, blank=True, null=True)
	jiaszssd = models.CharField(u'驾驶证所属地', max_length=100, blank=True, null=True)
	cundbh = models.CharField(u'存档编号', max_length=32, blank=True, null=True)
	beiz = models.CharField(u'备注', max_length=100, blank=True, null=True)

	car = models.ForeignKey(Car, blank=True, null=True)

	zhaop = models.ImageField(u'照片', upload_to='driver/zhaopian', blank=True, null=True)
	shenfzsm = models.ImageField(u'身份证扫描', upload_to='driver/shenfenzheng', blank=True, null=True)
	jiaszsm = models.ImageField(u'驾驶证扫描', upload_to='driver/jiashizheng', blank=True, null=True)
	fuwzgzsm = models.ImageField(u'服务资格证扫描', upload_to='driver/fuwuzigezheng', blank=True, null=True)

	valid = models.IntegerField(u'是否有效', default='1', editable=False)

	def delete(self, *args, **kwargs):
		storage, path = self.zhaop.storage, self.zhaop.path

		super(Driver, self).delete(*args, **kwargs)
		storage.delete(path)

		storage, path = self.shenfzsm.storage, self.shenfzsm.path

		super(Driver, self).delete(*args, **kwargs)
		storage.delete(path)

		storage, path = self.jiaszsm.storage, self.jiaszsm.path

		super(Driver, self).delete(*args, **kwargs)
		storage.delete(path)

		storage, path = self.fuwzgzsm.storage, self.fuwzgzsm.path

		super(Driver, self).delete(*args, **kwargs)
		storage.delete(path)

	def __unicode__(self):
		return self.jiasyxm

	class Meta:
		verbose_name = u'驾驶员信息'


class Driver_bargin(models.Model):
	#cheph = models.CharField(u'车牌号', max_length=20)
	#jiasyxm = models.CharField(u'驾驶员姓名', max_length=100)
	#shenfzh = models.CharField(u'身份证号', max_length=32)

	cars = models.ManyToManyField(Car)
	drivers = models.ManyToManyField(Driver)

	qiandsj = models.DateField(u'签订时间')
	hetqsrq = models.DateField(u'合同起始日期')
	hetzzrq = models.DateField(u'合同终止日期')
	anqbzj = models.DecimalField(u'安全保证金', max_digits=10, decimal_places=2, null=True, blank=True)
	weiyj = models.DecimalField(u'违约金', max_digits=10, decimal_places=2, null=True, blank=True)
	beiz = models.CharField(u'备注', max_length=100, null=True, blank=True)

	valid = models.IntegerField(u'是否有效', default='1', editable=False)

	def __unicode__(self):
		return self.cars.get().cheph + '  ' + self.drivers.get().jiasyxm

	class Meta:
		verbose_name = u'驾驶员合同'

class Driver_exam(models.Model):

	KAOHLB_CHOICES = (
			(u'营运', u'营运'),
			(u'表扬', u'表扬'),
			(u'其他', u'其他')
		)

	# chelid = models.IntegerField(u'车辆id')
	# cheph = models.CharField(u'车牌号', max_length=20)
	# jiasyid = models.IntegerField(u'驾驶员id')
	# jiasyxm = models.CharField(u'驾驶员姓名', max_length=100)
	#shenfzh = models.CharField(u'身份证号', max_length=32)

	cars = models.ManyToManyField(Car)
	drivers = models.ManyToManyField(Driver)

	kaohrq = models.DateField(u'考核日期')
	kaohlb = models.CharField(u'考核类别', max_length=32, choices=KAOHLB_CHOICES, null=True, blank=True)
	kaohnr = models.CharField(u'考核内容', max_length=100, null=True, blank=True)
	fens = models.DecimalField(u'分数', max_digits=6, decimal_places=2, null=True, blank=True)
	beiz = models.CharField(u'备注', max_length=100, null=True, blank=True)

	valid = models.IntegerField(u'是否有效', default='1', editable=False)

	def __unicode__(self):
		return self.cars.get().cheph + self.drivers.get().jiasyxm

	class Meta:
		verbose_name = u'驾驶员考核'









