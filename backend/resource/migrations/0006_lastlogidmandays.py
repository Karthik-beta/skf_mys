# Generated by Django 5.0.7 on 2024-10-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0005_mandaysattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastLogIdMandays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_log_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'last_log_id_mandays',
            },
        ),
    ]
