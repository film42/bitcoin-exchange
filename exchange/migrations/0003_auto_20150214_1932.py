# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_auto_20150208_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(max_digits=15, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(max_digits=15, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='limit',
            field=models.DecimalField(max_digits=13, decimal_places=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trade',
            name='rate',
            field=models.DecimalField(max_digits=15, decimal_places=8),
            preserve_default=True,
        ),
    ]
