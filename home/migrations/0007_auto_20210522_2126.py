# Generated by Django 3.1.7 on 2021-05-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210522_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration',
            name='keterangan',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='keterangan',
            field=models.TextField(blank=True),
        ),
    ]
