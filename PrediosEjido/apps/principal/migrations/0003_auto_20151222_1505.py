# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151222_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='c_recaja',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='f_recaja',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='v_recaja',
            field=models.DecimalField(max_digits=9, decimal_places=2, blank=True),
        ),
    ]
