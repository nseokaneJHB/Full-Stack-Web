# Generated by Django 3.1.6 on 2021-02-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(max_length=250),
        ),
    ]
