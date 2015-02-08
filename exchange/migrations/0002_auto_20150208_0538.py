# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeSecurity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('currency_type', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
                ('exchange', models.ForeignKey(to='exchange.Exchange')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='supportedexchangecurrency',
            name='exchange',
        ),
        migrations.DeleteModel(
            name='SupportedExchangeCurrency',
        ),
        migrations.AddField(
            model_name='trade',
            name='filled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
