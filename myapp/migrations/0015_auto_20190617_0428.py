# Generated by Django 2.0.8 on 2019-06-17 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20190617_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='2434'),
        ),
    ]
