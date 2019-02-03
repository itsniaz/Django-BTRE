# Generated by Django 2.1.5 on 2019-01-29 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('isMVP', models.BooleanField(default=False)),
                ('hireDate', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
