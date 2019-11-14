from core.settings import INSTALLED_APPS, REST_FRAMEWORK


DEVELOPING_APPS = [
    'django_extensions',
]

INSTALLED_APPS.extend(DEVELOPING_APPS)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].extend([
    'rest_framework.renderers.BrowsableAPIRenderer',
])

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].extend([
    'rest_framework.authentication.BasicAuthentication',
])
