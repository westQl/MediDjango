# Generated by Django 4.2.7 on 2023-11-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='DateOfBirth',
            field=models.DateField(max_length=10),
        ),
    ]