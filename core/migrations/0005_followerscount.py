# Generated by Django 4.1.3 on 2023-09-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_likepost'),
    ]

    operations = [
        migrations.CreateModel(
            name='followersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
            ],
        ),
    ]
