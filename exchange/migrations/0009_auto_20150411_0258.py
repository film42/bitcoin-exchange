# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='currency_type',
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='base_currency',
        ),
        migrations.RemoveField(
            model_name='exchangesecurity',
            name='currency_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='from_currency',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_type',
        ),
        migrations.RemoveField(
            model_name='order',
            name='side',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='to_currency',
        ),




        migrations.AddField(
            model_name='account',
            name='currency_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exchange',
            name='base_currency',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exchangesecurity',
            name='currency_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='from_currency',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='order_type',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='side',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='to_currency',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
