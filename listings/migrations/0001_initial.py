# Generated by Django 2.1.5 on 2019-01-29 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.DecimalField(decimal_places=1, max_digits=5)),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
