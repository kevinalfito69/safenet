# Generated by Django 5.0.6 on 2024-07-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannedIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('waktu', models.TimeField(auto_now_add=True)),
                ('service', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='IDPSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('waktu', models.TimeField(auto_now_add=True)),
                ('service', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='WaitList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('waktu', models.TimeField(auto_now_add=True)),
                ('service', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
