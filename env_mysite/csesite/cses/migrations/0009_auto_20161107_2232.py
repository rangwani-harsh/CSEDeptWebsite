# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0008_newsitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('idx', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('subevents', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='date',
            field=models.DateField(max_length=200, default=datetime.date(2016, 11, 7)),
        ),
    ]
