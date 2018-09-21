# Generated by Django 2.1.1 on 2018-09-21 05:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DonorAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(null=True)),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('days_since_created', models.IntegerField(blank=True, null=True)),
            ],
        ),
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
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='donoraccount',
            name='date_created',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='datecreated', to='signup.DonorInfo'),
        ),
        migrations.AddField(
            model_name='donoraccount',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='donorname', to='signup.DonorInfo'),
        ),
    ]
