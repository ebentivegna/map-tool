# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_tool', '0002_auto_20150709_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compsku',
            old_name='competitor_name',
            new_name='descr',
        ),
        migrations.RenameField(
            model_name='compsku',
            old_name='description',
            new_name='sellername',
        ),
        migrations.RenameField(
            model_name='compsku',
            old_name='sku_num',
            new_name='sku',
        ),
        migrations.RenameField(
            model_name='ksag',
            old_name='brand_name',
            new_name='brandname',
        ),
        migrations.RenameField(
            model_name='ksag',
            old_name='category_name',
            new_name='categoryname',
        ),
        migrations.RenameField(
            model_name='map',
            old_name='sku_num',
            new_name='sku',
        ),
        migrations.RemoveField(
            model_name='compsku',
            name='competitor_num',
        ),
        migrations.RemoveField(
            model_name='compsku',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='compsku',
            name='date_crawled',
        ),
        migrations.RemoveField(
            model_name='compsku',
            name='list_price',
        ),
        migrations.RemoveField(
            model_name='ksag',
            name='brand_num',
        ),
        migrations.RemoveField(
            model_name='ksag',
            name='category_num',
        ),
        migrations.RemoveField(
            model_name='ksag',
            name='ksag_num',
        ),
        migrations.RemoveField(
            model_name='map',
            name='base_percent',
        ),
        migrations.RemoveField(
            model_name='map',
            name='current_percent',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='percent',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sku',
            name='sku_num',
        ),
        migrations.AddField(
            model_name='compsku',
            name='curprice',
            field=models.CharField(default=0.0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compsku',
            name='date',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compsku',
            name='listprice',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compsku',
            name='sellerid',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ksag',
            name='brandid',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ksag',
            name='categoryid',
            field=models.CharField(default='', verbose_name='Ebisu category ID', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ksag',
            name='ksagid',
            field=models.CharField(max_length=10, serialize=False, default='', primary_key=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='basepercent',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='editorlink',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='percent',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='enddate',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='startdate',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sku',
            name='descr',
            field=models.CharField(default='', verbose_name='Item description', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sku',
            name='matchsku',
            field=models.CharField(serialize=False, max_length=20, default='', verbose_name='Blick SKU ID', primary_key=True),
            preserve_default=False,
        ),
    ]
