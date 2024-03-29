# Generated by Django 2.0.8 on 2019-06-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('depature', models.DateTimeField()),
                ('category', models.CharField(choices=[('AC sleeper', 'AC sleeper'), ('Non-AC sleeper', 'Non-AC sleeper'), ('AC Multi Axle Semi sleeper', 'AC Multi Axle Semi sleeper'), ('AC seater', 'AC seater')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('depature', models.DateTimeField()),
                ('category', models.CharField(choices=[('Super Luxery', 'Super Luxery'), ('Deluxe', 'Deluxe'), ('AC seater', 'AC seater')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('depature', models.DateTimeField()),
                ('category', models.CharField(choices=[('Non-AC sleeper', 'Non-AC sleeper'), ('AC Multi Axle Semi sleeper', 'AC Multi Axle Semi sleeper'), ('AC seater', 'AC seater')], max_length=30)),
            ],
        ),
    ]
