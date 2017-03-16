# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roombooker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Pending'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booked_by',
            field=models.CharField(max_length=50, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Your Email'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='end_time',
            field=models.IntegerField(verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='start_time',
            field=models.IntegerField(verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_image',
            field=models.ImageField(upload_to='roomimages'),
        ),
    ]