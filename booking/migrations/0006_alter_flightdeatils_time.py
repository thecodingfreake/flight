# Generated by Django 4.2.7 on 2024-01-02 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_flightdeatils'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdeatils',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
