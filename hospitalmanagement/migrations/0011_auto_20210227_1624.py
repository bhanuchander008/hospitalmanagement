# Generated by Django 3.1.7 on 2021-02-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagement', '0010_auto_20210227_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
