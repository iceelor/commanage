# Generated by Django 2.0.5 on 2019-03-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityRecord', '0003_auto_20190322_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberinfo',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=25, verbose_name='电话'),
        ),
    ]
