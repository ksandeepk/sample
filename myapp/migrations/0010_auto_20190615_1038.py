# Generated by Django 2.0.8 on 2019-06-15 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20190615_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elite',
            old_name='tim',
            new_name='bookd',
        ),
        migrations.RenameField(
            model_name='nor',
            old_name='tim',
            new_name='bookd',
        ),
        migrations.RenameField(
            model_name='pre',
            old_name='tim',
            new_name='bookd',
        ),
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='5121'),
        ),
    ]
