# Generated by Django 2.2.2 on 2020-02-07 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annote', '0003_auto_20200207_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='annotemodel',
            name='shape',
        ),
    ]
