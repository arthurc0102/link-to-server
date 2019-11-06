from django.conf import settings
from django.core.exceptions import ValidationError


TARGET = set(settings.CODE_TARGET)


def validate_code_in_target(value):
    not_valid_char = set(value) - TARGET
    if len(not_valid_char) != 0:
        raise ValidationError(
            '"{}" is not valid'.format(', '.join(not_valid_char)),
        )
