# Generated by Django 2.0.5 on 2019-04-11 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activityRecord', '0005_auto_20190411_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actrecord',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 14, 13, 13, 360311, tzinfo=utc), verbose_name='活动时间'),
        ),
    ]