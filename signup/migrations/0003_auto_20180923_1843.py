# Generated by Django 2.0.8 on 2018-09-23 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_remove_donorinfo_days_since_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='date_recvd',
            field=models.DateField(blank=True, null=True),
        ),
    ]
