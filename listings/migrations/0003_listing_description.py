# Generated by Django 2.2.5 on 2019-11-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20191111_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
