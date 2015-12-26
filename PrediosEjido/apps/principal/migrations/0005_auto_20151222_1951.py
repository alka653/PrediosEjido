# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20151222_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='c_recaja',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='d',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='e',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='f_recaja',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='v_recaja',
            field=models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True),
        ),
    ]
