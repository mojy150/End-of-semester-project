# Generated by Django 4.2.1 on 2023-08-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_actor_actor_alter_genre_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='director',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(max_length=50),
        ),
    ]