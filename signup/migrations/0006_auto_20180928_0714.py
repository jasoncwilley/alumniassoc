# Generated by Django 2.0.8 on 2018-09-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20180928_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorinfo',
            name='amount_recvd',
            field=models.IntegerField(default=0),
        ),
    ]
