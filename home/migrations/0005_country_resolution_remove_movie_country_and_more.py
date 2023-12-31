# Generated by Django 4.2.1 on 2023-08-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolution', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='resolution',
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ManyToManyField(related_name='country_rel_home', to='home.country'),
        ),
        migrations.AddField(
            model_name='movie',
            name='resolution',
            field=models.ManyToManyField(related_name='resolution_rel_home', to='home.resolution'),
        ),
    ]
