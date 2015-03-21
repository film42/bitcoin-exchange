# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('currency_type', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
                ('balance', models.DecimalField(max_digits=15, decimal_places=8)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
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
                'verbose_name': 'Exchange',
                'verbose_name_plural': 'Exchanges',
            },
            bases=(models.Model,),
        ),
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
                'verbose_name': 'ExchangeSecurity',
                'verbose_name_plural': 'ExchangeSecurities',
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
                ('amount', models.DecimalField(max_digits=15, decimal_places=8)),
                ('limit', models.DecimalField(max_digits=13, decimal_places=8)),
                ('from_currency', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
                ('to_currency', models.CharField(max_length=3, choices=[(b'1', b'BTC'), (b'0', b'USD')])),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name=b'Modified at')),
                ('rate', models.DecimalField(max_digits=15, decimal_places=8)),
                ('filled', models.BooleanField(default=False)),
                ('buy_order', models.ForeignKey(related_name='buy_order', to='exchange.Order')),
                ('sell_order', models.ForeignKey(related_name='sell_order', to='exchange.Order')),
            ],
            options={
                'verbose_name': 'Trade',
                'verbose_name_plural': 'Trades',
            },
            bases=(models.Model,),
        ),
    ]
