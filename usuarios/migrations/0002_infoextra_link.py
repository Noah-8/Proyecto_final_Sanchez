# Generated by Django 4.2.2 on 2023-07-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
