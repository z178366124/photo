from django.conf import settings

def is_app_installed(app_name):
    return app_name in settings.INSTALLED_APPS