# Generated by Django 5.0.6 on 2024-07-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('th_ssh', models.IntegerField(default=5)),
                ('th_flood', models.IntegerField(default=1000)),
            ],
        ),
    ]