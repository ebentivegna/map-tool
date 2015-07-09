# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompSku',
            fields=[
                ('sku_num', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('competitor_name', models.CharField(max_length=300)),
                ('competitor_num', models.IntegerField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_crawled', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ksag',
            fields=[
                ('ksag_num', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('category_num', models.IntegerField(verbose_name='Ebisu category ID')),
                ('category_name', models.CharField(max_length=300)),
                ('brand_num', models.IntegerField()),
                ('brand_name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('sku_num', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('base_percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('current_percent', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('name', models.CharField(max_length=300)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('sku_num', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('description', models.CharField(max_length=300)),
                ('ksag', models.ForeignKey(to='map_tool.Ksag')),
            ],
        ),
        migrations.AddField(
            model_name='promotion',
            name='parent_sku',
            field=models.ForeignKey(to='map_tool.Sku'),
        ),
        migrations.AddField(
            model_name='map',
            name='parent_sku',
            field=models.ForeignKey(to='map_tool.Sku'),
        ),
        migrations.AddField(
            model_name='compsku',
            name='parent_sku',
            field=models.ForeignKey(to='map_tool.Sku'),
        ),
    ]
