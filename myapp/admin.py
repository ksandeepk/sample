from django.contrib import admin
from .models import User,Elite,Pre,Nor,Bus

class UserAdmin(admin.ModelAdmin):
    list_display=['Passenger_name','username','password','category']

class EliteAdmin(admin.ModelAdmin):
    list_display=['source','destination','depature','category','seat_no']

class PreAdmin(admin.ModelAdmin):
    list_display=['source','destination','depature','category','bus_no','seat_no']

class NorAdmin(admin.ModelAdmin):
    list_display=['source','destination','depature','category','bus_no','seat_no']

class BusAdmin(admin.ModelAdmin):
    list_display=['source','category','bus_no']
admin.site.register(User,UserAdmin)
admin.site.register(Elite,EliteAdmin)
admin.site.register(Pre,PreAdmin)
admin.site.register(Nor,NorAdmin)
admin.site.register(Bus,BusAdmin)

# Register your models here.
