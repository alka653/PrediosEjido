# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='area_con',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='predio',
            name='d',
            field=models.CharField(max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='e',
            field=models.CharField(max_length=1, blank=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='hectarea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='predio',
            name='id_propieta_fin',
            field=models.ForeignKey(blank=True, to='principal.Propieta', null=True),
        ),
        migrations.AlterField(
            model_name='predio',
            name='id_propietario',
            field=models.CharField(default=b'0', max_length=15),
        ),
    ]
