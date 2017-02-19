# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EduDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('degree', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=60)),
                ('university', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('idx', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('projects', models.TextField(blank=True)),
                ('publications', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('from_year', models.CharField(max_length=20)),
                ('to_year', models.CharField(max_length=20)),
                ('inst', models.CharField(max_length=50)),
                ('desig', models.CharField(max_length=50)),
                ('idx', models.ForeignKey(to='cses.Faculty')),
            ],
        ),
        migrations.AddField(
            model_name='edudetails',
            name='idx',
            field=models.ForeignKey(to='cses.Faculty'),
        ),
    ]
