# Generated by Django 4.2.7 on 2023-12-02 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_patient_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.address'),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='patient',
            name='surname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DateOfBirth',
            field=models.DateField(default='2000-01-01'),
        ),
    ]