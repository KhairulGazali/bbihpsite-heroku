# Generated by Django 3.1.7 on 2021-05-19 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210519_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('keterangan', models.TextField()),
            ],
        ),
    ]
