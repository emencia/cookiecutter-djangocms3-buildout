# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('civility', models.IntegerField(verbose_name='civility', choices=[(0, 'mlle'), (1, 'mme'), (2, 'mr')])),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('message', models.TextField(verbose_name='message', blank=True)),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
                ('company', models.CharField(max_length=250, verbose_name='company', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='city', blank=True)),
                ('state', models.CharField(max_length=255, verbose_name='state/province', blank=True)),
                ('optin_newsletter', models.BooleanField(default=False, verbose_name='do you wish to receive the newsletter?')),
                ('country', models.ForeignKey(verbose_name='country', blank=True, to='countries.Country', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
