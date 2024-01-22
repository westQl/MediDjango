# Generated by Django 4.2.7 on 2024-01-09 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_dosage_medicine_alter_dosage_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='medicine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.medicine'),
        ),
        migrations.AlterField(
            model_name='dosage',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.patient'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='disease',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.disease'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.doctor'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.patient'),
        ),
    ]
