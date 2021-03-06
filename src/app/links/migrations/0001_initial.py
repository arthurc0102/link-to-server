# Generated by Django 2.2.7 on 2019-11-06 20:01

import app.links.services
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=app.links.services.generate_link_code, max_length=255, unique=True, validators=[utils.validators.validate_code_in_target])),
                ('url', models.URLField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('url', 'creator')},
            },
        ),
    ]
