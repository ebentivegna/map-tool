# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_tool', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sku',
            old_name='ksag',
            new_name='ksag_num',
        ),
        migrations.AlterField(
            model_name='compsku',
            name='competitor_num',
            field=models.IntegerField(),
        ),
    ]
