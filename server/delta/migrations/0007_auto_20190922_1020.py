# Generated by Django 2.2.3 on 2019-09-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0006_led'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='moisture',
            field=models.IntegerField(max_length=300),
        ),
    ]
