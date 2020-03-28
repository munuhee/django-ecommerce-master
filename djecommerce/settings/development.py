from demoproject.demoproject.settings import PROJECT_ROOT

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1',  '192.168.1.5', '6e0182f0.ngrok.io']

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')


def show_toolbar(request):
    return False


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306', }
}


STRIPE_Publishable_KEY = 'pk_test_ggIIsyni1nce2PSxs5mKgV8B00k6Jl9wpm'
STRIPE_SECRET_KEY = 'sk_test_s5jzUv8UPRMXrOTuOImwjtly00LggdjWOH'
ACCOUNT_EMAIL_VERIFICATION = "none"


