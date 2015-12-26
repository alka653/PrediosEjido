# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20151222_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='avaluo_catastral',
            field=models.DecimalField(max_digits=11, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='predio',
            name='v_recaja',
            field=models.DecimalField(max_digits=11, decimal_places=2, blank=True),
        ),
    ]
