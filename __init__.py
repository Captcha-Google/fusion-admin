import django

version = "0.1.1 Development"

if django.VERSION < (3, 2):
    default_app_config = "fusion.apps.FusionConfig"