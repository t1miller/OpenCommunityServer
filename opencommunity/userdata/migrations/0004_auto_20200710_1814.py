# Generated by Django 3.0.8 on 2020-07-10 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200709_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='username',
            new_name='creator',
        ),
    ]