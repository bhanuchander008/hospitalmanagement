# Generated by Django 3.1.7 on 2021-02-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalmanagement', '0002_auto_20210227_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
