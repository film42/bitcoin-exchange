# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_order_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='account',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=-1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
