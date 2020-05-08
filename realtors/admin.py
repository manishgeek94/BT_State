from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date')
    list_display_links = ('id',)
    search_fields = ('id','name')
    list_per_page = 10


admin.site.register(Realtor,RealtorAdmin)
