# Generated by Django 4.2.7 on 2023-12-02 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_city_address_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='DateOfBirth',
            new_name='date_of_birth',
        ),
    ]
