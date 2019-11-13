from django.contrib.auth import get_user_model
from django.db import models

from utils.validators import validate_code_in_target

from .services import generate_link_code


User = get_user_model()


class Link(models.Model):
    code = models.CharField(
        default=generate_link_code,
        max_length=255,
        unique=True,
        validators=[validate_code_in_target],
    )
    url = models.URLField()
    creator = models.ForeignKey(User, models.CASCADE, 'links', null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('url', 'creator'),
        )

    def __str__(self):
        return self.code
