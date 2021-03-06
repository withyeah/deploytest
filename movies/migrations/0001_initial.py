# Generated by Django 2.1.8 on 2019-05-17 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.TextField()),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('vote_average', models.FloatField(blank=True)),
                ('popularity', models.FloatField(blank=True)),
                ('poster_path', models.TextField(blank=True)),
                ('original_language', models.TextField(blank=True)),
                ('original_title', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
                ('release_date', models.TextField(blank=True)),
                ('backdrop_path', models.TextField(blank=True)),
                ('genre', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
