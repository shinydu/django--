# Generated by Django 2.1.1 on 2018-09-26 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20180926_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 17, 9, 33, 54382)),
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 17, 9, 33, 54382)),
        ),
    ]