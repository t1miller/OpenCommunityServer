# Generated by Django 3.0.8 on 2020-07-09 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200709_2051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Inbox',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
