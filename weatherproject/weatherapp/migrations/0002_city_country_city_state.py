# Generated by Django 4.1 on 2022-08-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='United States', max_length=25),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(default='New York', max_length=25),
        ),
    ]
