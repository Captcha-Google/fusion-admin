from django.contrib import admin
from .models import SiteVisitor,FusionConfiguration

class FusionAdmin(admin.AdminSite):
    site_header = 'Fusion Admin'


class AdminSiteVisitor(admin.ModelAdmin):
    list_display = ("visitor_ip","visitor_bowser_platform","visitor_date_added",)
    search_fields = ("visitor_ip","visitor_bowser_platform",)
    list_filter = ("visitor_bowser_platform",)

class AdminFusionConfiguration(admin.ModelAdmin):
    list_display = ("site_name","site_author","date_added",)
    search_fields = ("site_name","site_author",)

admin.site.register(FusionConfiguration,AdminFusionConfiguration)
admin.site.register(SiteVisitor,AdminSiteVisitor)

