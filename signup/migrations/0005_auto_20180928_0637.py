# Generated by Django 2.0.8 on 2018-09-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_donorinfo_amount_recvd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='amount_recvd',
            field=models.IntegerField(null=True),
        ),
    ]