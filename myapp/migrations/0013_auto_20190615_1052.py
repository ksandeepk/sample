# Generated by Django 2.0.8 on 2019-06-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190615_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='4130'),
        ),
    ]
