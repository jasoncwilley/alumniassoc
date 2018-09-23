# Generated by Django 2.0.8 on 2018-09-23 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('street_address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('email', models.EmailField(blank=True, max_length=35, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('days_since_created', models.IntegerField(blank=True, null=True)),
                ('payment_recvd', models.NullBooleanField()),
                ('date_recvd', models.DateField(null=True)),
            ],
        ),
    ]
