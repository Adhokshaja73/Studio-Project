# Generated by Django 5.1 on 2024-08-31 19:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_bookingsession_bookingdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studio',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='bookingsession',
            name='bookingDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 1, 18, 58, 493289)),
        ),
        migrations.AlterField(
            model_name='bookingsession',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 1, 18, 58, 493289)),
        ),
        migrations.AlterField(
            model_name='bookingsession',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 1, 18, 58, 493289)),
        ),
        migrations.AlterField(
            model_name='bookingsessionchat',
            name='messageDatetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 1, 18, 58, 493289)),
        ),
        migrations.AlterField(
            model_name='bookingsessionpayment',
            name='paymentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 1, 18, 58, 493289)),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='userType',
            field=models.IntegerField(choices=[(1, 'Studio Owner'), (2, 'User')], default=2),
        ),
    ]
