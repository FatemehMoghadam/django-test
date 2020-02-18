# Generated by Django 3.0.3 on 2020-02-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thecut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(default='', max_length=40),
        ),
    ]