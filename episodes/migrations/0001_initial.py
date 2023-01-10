# Generated by Django 4.1.5 on 2023-01-10 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('video_hd_url', models.TextField()),
                ('video_sd_url', models.TextField()),
                ('anime', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='animes.anime')),
            ],
        ),
    ]
