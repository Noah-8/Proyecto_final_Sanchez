# Generated by Django 4.2.2 on 2023-07-15 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_teclados_teclado'),
    ]

    operations = [
        migrations.AddField(
            model_name='teclado',
            name='autor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teclado',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
