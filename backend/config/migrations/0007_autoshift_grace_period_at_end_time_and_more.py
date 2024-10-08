# Generated by Django 5.0.7 on 2024-09-13 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_alter_shift_lunch_duration_alter_shift_lunch_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoshift',
            name='grace_period_at_end_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='autoshift',
            name='grace_period_at_start_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
