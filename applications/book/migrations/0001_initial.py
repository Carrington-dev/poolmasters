# Generated by Django 4.2.7 on 2023-11-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_recieved', models.DateTimeField(auto_now_add=True, verbose_name='date recieved')),
                ('date_last_viewed', models.DateTimeField(auto_now=True, verbose_name='last viewed')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('is_subscribed', models.BooleanField(default=True, verbose_name='subscribed')),
                ('date_recieved', models.DateTimeField(auto_now_add=True, verbose_name='date recieved')),
                ('date_last_viewed', models.DateTimeField(auto_now=True, verbose_name='last viewed')),
            ],
            options={
                'verbose_name': 'Subscribe',
                'verbose_name_plural': 'Subscribes',
            },
        ),
    ]