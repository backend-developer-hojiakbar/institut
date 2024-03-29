# Generated by Django 4.2.1 on 2023-09-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_patent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moddalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moddaSoni', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
                ('about', models.CharField(max_length=250)),
                ('link', models.URLField(max_length=300)),
            ],
        ),
    ]