# Generated by Django 4.0.2 on 2022-02-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reveurs', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_picture',
            field=models.TextField(default='null'),
        ),
    ]
