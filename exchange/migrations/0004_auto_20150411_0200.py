# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_remove_order_guid'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='guid',
            field=uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='guid',
            field=uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=False),
            preserve_default=True,
        ),
    ]
