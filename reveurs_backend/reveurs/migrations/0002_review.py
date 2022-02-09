# Generated by Django 4.0.2 on 2022-02-09 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reveurs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reveurs.location')),
            ],
        ),
    ]