# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0002_faculty_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='desig',
            field=models.CharField(max_length=50, default='Professor'),
            preserve_default=False,
        ),
    ]
