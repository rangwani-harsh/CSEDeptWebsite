# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0005_auto_20161105_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='image',
        ),
    ]
