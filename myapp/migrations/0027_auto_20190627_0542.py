# Generated by Django 2.0.8 on 2019-06-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20190627_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='8396'),
        ),
    ]
