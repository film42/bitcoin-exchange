# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_remove_account_guid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='guid',
        ),
    ]
