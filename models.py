from django.db import models

class SiteVisitor(models.Model):
    visitor_ip = models.GenericIPAddressField(serialize=True)
    visitor_user_agent = models.TextField(max_length=255)
    visitor_bowser = models.CharField(max_length=255)
    visitor_bowser_platform = models.CharField(max_length=255)
    visitor_date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.visitor_ip
    
    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'
        ordering = ['-visitor_date_added']

    
class FusionConfiguration(models.Model):
    site_favicon = models.ImageField(upload_to="fusion/static/img/site/img")
    site_icon = models.ImageField(upload_to="fusion/static/img/site/img")
    site_name = models.CharField(max_length=255)
    site_status = models.CharField(max_length=50)
    site_description = models.TextField(max_length=255)
    site_author = models.CharField(max_length=100)
    site_keyword = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Configuration'
        verbose_name_plural = 'Configurations'
        ordering = ['-date_added']