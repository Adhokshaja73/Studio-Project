# Generated by Django 5.1 on 2024-09-01 10:59

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_studio_city_alter_bookingsession_bookingdate_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingsessionpayment',
            name='bookingSession',
        ),
        migrations.RemoveField(
            model_name='bookingsessionuserrelation',
            name='bookingSession',
        ),
        migrations.RemoveField(
            model_name='bookingsessionchat',
            name='bookingSession',
        ),
        migrations.AlterField(
            model_name='bookingsessionchat',
            name='messageDatetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 16, 28, 52, 810775)),
        ),
        migrations.AlterField(
            model_name='bookingsessionpayment',
            name='paymentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 1, 16, 28, 52, 810775)),
        ),
        migrations.CreateModel(
            name='CalendarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Booked'), (2, 'Cancelled')])),
                ('bookingDate', models.DateTimeField(default=datetime.datetime(2024, 9, 1, 16, 28, 52, 809776))),
                ('startTime', models.DateTimeField(default=datetime.datetime(2024, 9, 1, 16, 28, 52, 809776))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2024, 9, 1, 16, 28, 52, 809776))),
                ('bookedByUser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.studio')),
            ],
        ),
        migrations.AddField(
            model_name='bookingsessionchat',
            name='calendarItem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='main.calendaritem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingsessionpayment',
            name='calendarItem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='main.calendaritem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingsessionuserrelation',
            name='calendarItem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='main.calendaritem'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BookingSession',
        ),
    ]
