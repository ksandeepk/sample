# Generated by Django 2.0.8 on 2019-06-19 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20190619_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elite',
            name='bus_no',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Bus'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='0851'),
        ),
    ]
