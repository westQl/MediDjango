# Generated by Django 4.2.7 on 2023-12-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_rename_property_disease_symptoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='symptoms',
            field=models.CharField(max_length=50, null=True),
        ),
    ]