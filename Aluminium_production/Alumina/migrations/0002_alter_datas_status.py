# Generated by Django 5.1.2 on 2024-10-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
