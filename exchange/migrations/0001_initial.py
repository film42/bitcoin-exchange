# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('currency_type', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
                ('balance', models.DecimalField(max_digits=100000000000000, decimal_places=2)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('api_url', models.CharField(max_length=255)),
                ('base_currency', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('order_type', models.CharField(max_length=1, choices=[(b'1', b'Limit'), (b'0', b'Market')])),
                ('side', models.CharField(max_length=1, choices=[(b'0', b'Buy'), (b'1', b'Sell')])),
                ('amount', models.DecimalField(max_digits=100000000000000, decimal_places=2)),
                ('limit', models.DecimalField(max_digits=1000000000000, decimal_places=2)),
                ('from_currency', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
                ('to_currency', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SupportedExchangeCurrency',
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
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('rate', models.DecimalField(max_digits=10000000000, decimal_places=2)),
                ('buy_order', models.ForeignKey(related_name='buy_order', to='exchange.Order')),
                ('sell_order', models.ForeignKey(related_name='sell_order', to='exchange.Order')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'BaseModel',
                'verbose_name_plural': 'BaseModels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(to='exchange.User'),
            preserve_default=True,
        ),
    ]
