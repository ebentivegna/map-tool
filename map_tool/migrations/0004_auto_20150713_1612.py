# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_tool', '0003_auto_20150713_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compsku',
            name='curprice',
            field=models.CharField(max_length=10, verbose_name='Current price'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='date',
            field=models.CharField(max_length=10, verbose_name='Date crawled'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='descr',
            field=models.CharField(max_length=300, verbose_name='Item description'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='listprice',
            field=models.CharField(max_length=10, verbose_name='List price'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='sellerid',
            field=models.CharField(max_length=10, verbose_name='Seller ID'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='sellername',
            field=models.CharField(max_length=300, verbose_name='Seller name'),
        ),
        migrations.AlterField(
            model_name='compsku',
            name='sku',
            field=models.CharField(primary_key=True, verbose_name='SKU ID', serialize=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='ksag',
            name='brandid',
            field=models.CharField(max_length=10, verbose_name='Brand ID'),
        ),
        migrations.AlterField(
            model_name='ksag',
            name='brandname',
            field=models.CharField(max_length=300, verbose_name='Brand name'),
        ),
        migrations.AlterField(
            model_name='ksag',
            name='categoryname',
            field=models.CharField(max_length=300, verbose_name='Ebisu category name'),
        ),
        migrations.AlterField(
            model_name='ksag',
            name='ksagid',
            field=models.CharField(primary_key=True, verbose_name='KSAG ID', serialize=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='ksag',
            name='name',
            field=models.CharField(max_length=300, verbose_name='KSAG name'),
        ),
        migrations.AlterField(
            model_name='map',
            name='basepercent',
            field=models.CharField(max_length=5, verbose_name='Base percent discount'),
        ),
        migrations.AlterField(
            model_name='map',
            name='editorlink',
            field=models.CharField(max_length=200, verbose_name='Ebisu editor link'),
        ),
        migrations.AlterField(
            model_name='map',
            name='percent',
            field=models.CharField(max_length=5, verbose_name='Current percent discount'),
        ),
        migrations.AlterField(
            model_name='map',
            name='sku',
            field=models.CharField(primary_key=True, verbose_name='SKU ID', serialize=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='enddate',
            field=models.CharField(max_length=10, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Promotion name'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='startdate',
            field=models.CharField(max_length=10, verbose_name='Start date'),
        ),
    ]
