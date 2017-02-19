# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0006_remove_faculty_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.ImageField(upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='areas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
