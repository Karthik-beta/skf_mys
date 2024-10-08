# Generated by Django 5.0.4 on 2024-07-30 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_shift_mid_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autoshift',
            old_name='grace_period_after_start_time',
            new_name='full_day_threshold',
        ),
        migrations.RenameField(
            model_name='autoshift',
            old_name='grace_period_after_end_time',
            new_name='half_day_threshold',
        ),
        migrations.RenameField(
            model_name='autoshift',
            old_name='grace_period_before_end_time',
            new_name='lunch_duration',
        ),
        migrations.RenameField(
            model_name='autoshift',
            old_name='grace_period_before_start_time',
            new_name='overtime_threshold_after_end',
        ),
        migrations.RenameField(
            model_name='autoshift',
            old_name='overtime_threshold',
            new_name='overtime_threshold_before_start',
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='grace_period',
            new_name='full_day_threshold',
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='overtime_threshold',
            new_name='grace_period_at_end_time',
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='mid_day',
            new_name='lunch_in',
        ),
        migrations.AddField(
            model_name='autoshift',
            name='lunch_in',
            field=models.TimeField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autoshift',
            name='lunch_out',
            field=models.TimeField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autoshift',
            name='night_shift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='autoshift',
            name='tolerance_end_time',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='autoshift',
            name='tolerance_start_time',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='grace_period_at_start_time',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='half_day_threshold',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='lunch_duration',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='lunch_out',
            field=models.TimeField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='night_shift',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shift',
            name='overtime_threshold_after_end',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='overtime_threshold_before_start',
            field=models.DurationField(default=datetime.time(13, 0)),
            preserve_default=False,
        ),
    ]
