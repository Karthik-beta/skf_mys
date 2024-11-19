# Generated by Django 5.0.7 on 2024-11-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0007_mandaysmissedpunchattendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Training', 'Training'), ('Confirmed', 'Confirmed'), ('Professional', 'Professional'), ('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employeeid', 'logdate')},
        ),
        migrations.AlterUniqueTogether(
            name='mandaysattendance',
            unique_together={('employeeid', 'logdate')},
        ),
    ]
