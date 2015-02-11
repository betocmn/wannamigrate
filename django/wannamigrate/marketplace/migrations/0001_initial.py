# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_preferred_timezone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('gross_total', models.DecimalField(max_digits=5, verbose_name='gross total', decimal_places=2)),
                ('net_total', models.DecimalField(max_digits=5, verbose_name='net total', decimal_places=2)),
                ('discount', models.DecimalField(max_digits=5, verbose_name='discount', decimal_places=2)),
                ('fees', models.DecimalField(max_digits=5, verbose_name='fees', decimal_places=2)),
                ('installments', models.SmallIntegerField(verbose_name='installments', default=1)),
                ('external_code', models.CharField(verbose_name='external code', max_length=100)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('transaction_code', models.CharField(verbose_name='transaction code', max_length=100)),
                ('payment_code', models.CharField(verbose_name='payment code', max_length=100)),
                ('message', models.TextField(blank=True, verbose_name='message', null=True)),
                ('order', models.ForeignKey(to='marketplace.Order', verbose_name='order')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=45)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='code', max_length=15)),
                ('discount', models.DecimalField(max_digits=5, verbose_name='discount', decimal_places=2)),
                ('expiry_date', models.DateField(verbose_name='date')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('display_name', models.CharField(verbose_name='name', max_length=80)),
                ('headline', models.CharField(verbose_name='headline', max_length=150)),
                ('description', models.TextField(verbose_name='description')),
                ('skype_username', models.CharField(blank=True, max_length=100, verbose_name='skype ID', null=True)),
                ('paypal_email', models.EmailField(blank=True, max_length=75, verbose_name='paypal email', null=True)),
                ('website', models.URLField(blank=True, verbose_name='website', null=True)),
                ('countries', models.ManyToManyField(to='core.Country')),
                ('languages', models.ManyToManyField(to='core.Language')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider_ServiceTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('is_top', models.BooleanField(verbose_name='is top service', default=False)),
                ('provider', models.ForeignKey(to='marketplace.Provider', verbose_name='provider')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Regulator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=80)),
                ('website', models.URLField(blank=True, verbose_name='website', null=True)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('score', models.SmallIntegerField(verbose_name='review score', default=0)),
                ('comment', models.TextField(verbose_name='comment')),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='from user', related_name='review_from_user')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='to user', related_name='review_to_user')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('service_price', models.DecimalField(max_digits=5, verbose_name='service price', decimal_places=2)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='from user', related_name='service_from_user')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('service', models.ForeignKey(to='marketplace.Service', verbose_name='service')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=45)),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='name', max_length=60)),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'default_permissions': [],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servicehistory',
            name='service_status',
            field=models.ForeignKey(to='marketplace.ServiceStatus', verbose_name='service status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicehistory',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='changed by user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='history',
            field=models.ManyToManyField(to='marketplace.ServiceStatus', through='marketplace.ServiceHistory', related_name='history'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='service_status',
            field=models.ForeignKey(to='marketplace.ServiceStatus', verbose_name='service status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(to='marketplace.ServiceType', verbose_name='service type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='to_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='to user', related_name='service_to_user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider_servicetypes',
            name='service_type',
            field=models.ForeignKey(to='marketplace.ServiceType', verbose_name='service type'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='provider_servicetypes',
            unique_together=set([('service_type', 'provider')]),
        ),
        migrations.AddField(
            model_name='provider',
            name='regulator',
            field=models.ForeignKey(to='marketplace.Regulator', verbose_name='regulator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='service_types',
            field=models.ManyToManyField(to='marketplace.ServiceType', through='marketplace.Provider_ServiceTypes', related_name='service_types'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='order_status',
            field=models.ForeignKey(to='marketplace.OrderStatus', verbose_name='order status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='history',
            field=models.ManyToManyField(to='marketplace.OrderStatus', through='marketplace.OrderHistory', related_name='history'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(to='marketplace.OrderStatus', verbose_name='order status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.ForeignKey(to='marketplace.PromoCode', blank=True, null=True, verbose_name='promo code'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(to='marketplace.Service', verbose_name='service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=True,
        ),
    ]
