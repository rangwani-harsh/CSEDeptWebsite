# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cses', '0011_auto_20161112_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('cscoursecode', models.CharField(max_length=20)),
                ('coursecode', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('contacthours', models.CharField(max_length=20)),
                ('credits', models.IntegerField()),
                ('sem', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='eventitem',
            name='image',
            field=models.ImageField(upload_to='', default='1.jpg'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(upload_to='', default='1.jpg'),
            preserve_default=False,
        ),
    ]
