# Generated by Django 2.1.5 on 2019-02-21 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190131_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 23, 54, 28, 418326)),
        ),
    ]
