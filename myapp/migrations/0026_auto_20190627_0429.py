# Generated by Django 2.0.8 on 2019-06-27 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_auto_20190620_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='1947'),
        ),
    ]
