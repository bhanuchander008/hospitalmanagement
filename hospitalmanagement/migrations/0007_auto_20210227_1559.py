# Generated by Django 3.1.7 on 2021-02-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagement', '0006_auto_20210227_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(max_length=50),
        ),
    ]
