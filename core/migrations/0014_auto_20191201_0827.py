# Generated by Django 2.2.6 on 2019-12-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191201_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseitem',
            name='pdf',
            field=models.FileField(blank=True, default='', null='True', upload_to='media'),
        ),
    ]
