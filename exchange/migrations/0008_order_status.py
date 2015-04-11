# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0007_auto_20150411_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'0', max_length=3, choices=[(b'2', b'COMPLETE'), (b'0', b'NONE'), (b'1', b'PARTIAL')]),
            preserve_default=True,
        ),
    ]
