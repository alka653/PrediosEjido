# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_catastral', models.CharField(max_length=15)),
                ('t_ord', models.CharField(max_length=3)),
                ('t_tot', models.CharField(max_length=3)),
                ('propieta', models.CharField(max_length=50)),
                ('e', models.CharField(max_length=1)),
                ('d', models.CharField(max_length=1)),
                ('id_propietario', models.CharField(max_length=15)),
                ('dir_predio', models.CharField(max_length=30)),
                ('hectarea', models.IntegerField()),
                ('met2', models.IntegerField()),
                ('area_con', models.IntegerField()),
                ('avaluo_catastral', models.DecimalField(max_digits=9, decimal_places=2)),
                ('c_recaja', models.IntegerField()),
                ('f_recaja', models.DateField()),
                ('v_recaja', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Propieta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_propieta', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='predio',
            name='id_propieta_fin',
            field=models.ForeignKey(to='principal.Propieta', null=True),
        ),
    ]
