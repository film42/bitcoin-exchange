# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_auto_20150411_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='guid',
            field=uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
