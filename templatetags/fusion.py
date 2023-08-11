from typing import Any, Callable, Dict, Optional, Union
from django.contrib.admin.sites import all_sites
from django.contrib.auth.models import AbstractUser
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.template import Context, Library

from django.templatetags.static import static

from fusion.settings import get_settings
from .. import version

register = Library()

@register.simple_tag
def get_fusion_version() -> str:
    return version


@register.simple_tag
def get_site_name() -> str:
    return "FusionAdmin"

@register.simple_tag
def get_user_avatar(user: AbstractUser) -> str:

    no_avatar = static("admin/img/avatars/avatar.jpg")
    options = get_settings()
    avatar_field_name: Optional[Union[str, Callable]] = options.get("user_avatar")

    if not avatar_field_name:
        return no_avatar

    if callable(avatar_field_name):
        return avatar_field_name(user)
    
@register.simple_tag
def get_fusion_settings(request: WSGIRequest) -> Dict:
    """
    Get Fusion settings, update any defaults from the request, and return
    """
    settings = get_settings()

    admin_site = {x.name: x for x in all_sites}.get("admin", {})
    if not settings["site_title"]:
        settings["site_title"] = getattr(admin_site, "site_title", None)

    if not settings["site_header"]:
        settings["site_header"] = getattr(admin_site, "site_header", None)

    if not settings["site_brand"]:
        settings["site_brand"] = getattr(admin_site, "site_header", None)

    return settings

@register.filter
def has_fusion_setting(settings: Dict[str, Any], key: str) -> bool:
    return key in settings and settings[key] is not None


@register.simple_tag
def get_users():
    return User.objects.all()


