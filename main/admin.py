from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from main.models import Locomotive, Branch, Mileage

AdminSite.site_header = 'Локомотивные технологии'
AdminSite.site_title = 'Локомотивные технологии'


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Locomotive)
class LocomotiveAdmin(admin.ModelAdmin):
    list_display = ('series', 'branch', 'rate')


@admin.register(Mileage)
class MileageAdmin(admin.ModelAdmin):
    list_display = ('locomotive', 'year', 'value')
