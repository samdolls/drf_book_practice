# Generated by Django 4.2.3 on 2023-07-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter5', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
