# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_trade_guid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='account',
            field=models.ForeignKey(default=1, to='exchange.Account'),
            preserve_default=False,
        ),
    ]
