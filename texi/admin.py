from django.contrib import admin
from texi.models import Notification, Driver, Driver_bargin, Driver_exam, Car



class NotificationAdmin(admin.ModelAdmin):
	pass

class DriverAdmin(admin.ModelAdmin):
	pass

class Driver_bargin_Admin(admin.ModelAdmin):
	pass

class Driver_exam_Admin(admin.ModelAdmin):
	pass

class CarAdmin(admin.ModelAdmin):
	pass

admin.site.register(Notification, NotificationAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Driver_bargin, Driver_bargin_Admin)
admin.site.register(Driver_exam, Driver_exam_Admin)

admin.site.register(Car, CarAdmin)