# Generated by Django 4.2.7 on 2024-01-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_alter_flightdeatils_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='flightbookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=2080)),
                ('refno', models.CharField(max_length=2080)),
                ('name', models.CharField(max_length=2080)),
                ('time', models.TimeField()),
                ('fromp', models.CharField(max_length=2080)),
                ('top', models.CharField(max_length=2080)),
                ('date', models.DateField()),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='flightdeatils',
            name='refno',
            field=models.CharField(default='123', max_length=2080),
        ),
    ]
