# Generated by Django 2.2.2 on 2020-02-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annote', '0005_annotemodel_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotemodel',
            name='garbage',
            field=models.CharField(default='Garbage', max_length=30),
        ),
    ]
