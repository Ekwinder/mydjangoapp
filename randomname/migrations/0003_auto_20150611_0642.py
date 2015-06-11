# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomname', '0002_auto_20150611_0639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='date',
            new_name='xname',
        ),
    ]
