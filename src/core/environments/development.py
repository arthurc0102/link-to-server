from core.settings import REST_FRAMEWORK


REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].extend([
    'rest_framework.renderers.BrowsableAPIRenderer',
])

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].extend([
    'rest_framework.authentication.BasicAuthentication',
])
