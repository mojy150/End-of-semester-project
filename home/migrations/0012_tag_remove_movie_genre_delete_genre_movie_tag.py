# Generated by Django 4.1.3 on 2023-08-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_genre_genre_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, unique=True)),
                ('tag_url', models.CharField(default='/search?q=', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_rel_home', to='home.tag'),
        ),
    ]
