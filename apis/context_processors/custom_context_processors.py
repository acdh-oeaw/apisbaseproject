import sys
import inspect

from django.conf import settings


def add_entities(request):
    ent_list = []
    for name, obj in inspect.getmembers(sys.modules['entities.models'], inspect.isclass):
        if obj.__module__ == 'entities.models':
            ent_list.append(str(name).lower())
    res = {
        'entities_list': ent_list,
        'request': request
    }
    return res


def add_apis_settings(request):
    """adds the custom settings to the templates"""
    res = {
        'additional_functions': getattr(settings, "APIS_COMPONENTS", []),
        'request': request
    }
    if 'apis_highlighter' in settings.INSTALLED_APPS:
        res['highlighter_active'] = True
    else:
        res['highlighter_active'] = False
    return res
