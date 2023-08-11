import copy
import logging
from typing import Dict, Any

from django.conf import settings
from django.templatetags.static import static

from fusion.utils import get_admin_url, get_model_meta

logger = logging.getLogger(__name__)

DEFAULT_SETTINGS: Dict[str, Any] = {
    "site_title": None,
    "site_header": None,
    "site_brand": None,
    "site_logo": "",
    "site_icon": None,
    "welcome_sign": "Welcome",
    "copyright": "",
    "search_model": None,
    "user_avatar": None,
    "custom_links": {},
    "icons": {"auth": "users", "auth.user": "user", "auth.Group": "users"},
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
}

def get_search_model_string(search_model: str) -> str:
    """
    Get a search model string for reversing an admin url.

    Ensure the model name is lower cased but remain the app name untouched.
    """

    app, model_name = search_model.split(".")
    return "{app}.{model_name}".format(app=app, model_name=model_name.lower())

def get_settings() -> Dict:
    fusion_settings = copy.deepcopy(DEFAULT_SETTINGS)
    user_settings = {x: y for x, y in getattr(settings, "FUSION_SETTINGS", {}).items() if y is not None}
    fusion_settings.update(user_settings)

    # Extract search model configuration from search_model setting
    if fusion_settings["search_model"]:
        if not isinstance(fusion_settings["search_model"], list):
            fusion_settings["search_model"] = [fusion_settings["search_model"]]

        fusion_settings["search_models_parsed"] = []

        for search_model in fusion_settings["search_model"]:
            fusion_search_model = {}
            fusion_search_model["search_url"] = get_admin_url(get_search_model_string(search_model))

            model_meta = get_model_meta(search_model)
            if model_meta:
                fusion_search_model["search_name"] = model_meta.verbose_name_plural.title()
            else:
                fusion_search_model["search_name"] = search_model.split(".")[-1] + "s"
            fusion_settings["search_models_parsed"].append(fusion_search_model)

    # Ensure icon model names and classes are lower case
    fusion_settings["icons"] = {x.lower(): y.lower() for x, y in fusion_settings.get("icons", {}).items()}

    # Default the site icon using the site logo
    fusion_settings["site_icon"] = fusion_settings["site_icon"] or fusion_settings["site_logo"]


    return fusion_settings
