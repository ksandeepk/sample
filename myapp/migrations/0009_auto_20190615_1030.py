# Generated by Django 2.0.8 on 2019-06-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20190615_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='elite',
            name='seat_no',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='elite',
            name='tim',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nor',
            name='seat_no',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='nor',
            name='tim',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pre',
            name='seat_no',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='', max_length=30),
        ),
        migrations.AddField(
            model_name='pre',
            name='tim',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pid',
            field=models.IntegerField(default='0585'),
        ),
    ]