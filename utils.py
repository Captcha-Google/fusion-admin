import logging
from typing import List, Union, Dict, Set, Callable, Any
from urllib.parse import urlencode

from django.apps import apps
from django.contrib.admin import ListFilter
from django.contrib.admin.helpers import AdminForm
from django.contrib.auth.models import AbstractUser
from django.db.models.base import ModelBase, Model
from django.db.models.options import Options
from django.utils.translation import gettext

from fusion.compat import NoReverseMatch, reverse

logger = logging.getLogger(__name__)


def get_model_meta(model_str: str) -> Union[None, Options]:
    """
    Get model meta class
    """
    try:
        app, model = model_str.split(".")
        model_klass: Model = apps.get_registered_model(app, model)
        return model_klass._meta
    except (ValueError, LookupError):
        return None
    
def get_admin_url(instance: Any, admin_site: str = "admin", from_app: bool = False, **kwargs: str) -> str:
    """
    Return the admin URL for the given instance, model class or <app>.<model> string
    """
    url = "#"

    try:

        if type(instance) == str:
            app_label, model_name = instance.split(".")
            model_name = model_name.lower()
            url = reverse(
                "admin:{app_label}_{model_name}_changelist".format(app_label=app_label, model_name=model_name),
                current_app=admin_site,
            )

        # Model class
        elif instance.__class__ == ModelBase:
            app_label, model_name = instance._meta.app_label, instance._meta.model_name
            url = reverse(
                "admin:{app_label}_{model_name}_changelist".format(app_label=app_label, model_name=model_name),
                current_app=admin_site,
            )

        # Model instance
        elif instance.__class__.__class__ == ModelBase and isinstance(instance, instance.__class__):
            app_label, model_name = instance._meta.app_label, instance._meta.model_name
            url = reverse(
                "admin:{app_label}_{model_name}_change".format(app_label=app_label, model_name=model_name),
                args=(instance.pk,),
                current_app=admin_site,
            )

    except (NoReverseMatch, ValueError):
        # If we are not walking through the models within an app, let the user know this url cant be reversed
        if not from_app:
            logger.warning(gettext("Could not reverse url from {instance}".format(instance=instance)))

    if kwargs:
        url += "?{params}".format(params=urlencode(kwargs))

    return url