# Generated by Django 2.0.8 on 2019-06-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20190619_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='8845'),
        ),
    ]