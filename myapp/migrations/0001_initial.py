# Generated by Django 3.1.3 on 2020-11-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('species', models.CharField(choices=[('fish', 'Chum'), ('fish', 'Coho'), ('fish', 'Chinook'), ('fish', 'Pink'), ('fish', 'Sockeye'), ('fish', 'Trout')], max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=300)),
            ],
        ),
    ]
