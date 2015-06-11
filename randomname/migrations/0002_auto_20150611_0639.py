# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomname', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='date',
            field=models.CharField(default=1, max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
