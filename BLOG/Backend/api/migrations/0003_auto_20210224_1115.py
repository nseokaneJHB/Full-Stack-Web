# Generated by Django 3.1.6 on 2021-02-24 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210224_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='last_name',
        ),
    ]
