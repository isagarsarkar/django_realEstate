# Generated by Django 2.2.5 on 2019-11-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=2),
        ),
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='listing',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5),
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
