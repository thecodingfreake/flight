# Generated by Django 4.2.7 on 2024-01-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_flightdeatils_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdeatils',
            name='time',
            field=models.TimeField(),
        ),
    ]
