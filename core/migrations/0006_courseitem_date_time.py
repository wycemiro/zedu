# Generated by Django 2.2.6 on 2019-11-27 19:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191127_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseitem',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
