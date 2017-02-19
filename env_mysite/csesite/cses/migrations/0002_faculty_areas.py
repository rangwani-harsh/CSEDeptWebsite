# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='areas',
            field=models.TextField(default='CSE'),
            preserve_default=False,
        ),
    ]
