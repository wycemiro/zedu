# Generated by Django 2.2.6 on 2019-12-01 06:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191201_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseitem',
            name='github',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
    ]
