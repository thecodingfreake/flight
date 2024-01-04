from django.contrib import admin
from .models import *
# Register your models here.
class customerAdmin(admin.ModelAdmin):
    list_display=('name','password','email')

class flightdeatilsAdmin(admin.ModelAdmin):
    list_display=('name','refno','time','fromp','top','date','seats')
class flightbookingsAdmin(admin.ModelAdmin):
    list_display=('user','refno','name','time','fromp','top','date','seats')
admin.site.register(customer,customerAdmin)
admin.site.register(flightdeatils,flightdeatilsAdmin)
admin.site.register(flightbookings,flightbookingsAdmin)