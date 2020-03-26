import random

from django.apps import apps
from django.conf import settings


CODE_LEN = settings.CODE_LEN
CODE_TARGET = settings.CODE_TARGET


def generate_code():
    return ''.join([random.choice(CODE_TARGET) for _ in range(CODE_LEN)])


def generate_code_for_model(app_label, model_name, field='code'):
    code = None
    model = apps.get_model(app_label, model_name)

    while code is None or model.objects.filter(**{field: code}).exists():
        code = generate_code()

    return code
