# Generated by Django 3.2.6 on 2021-08-28 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diabetic_clinic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diabeteshistory',
            old_name='details',
            new_name='other_diabetic_complication',
        ),
        migrations.RenameField(
            model_name='medicalhistory',
            old_name='remarks',
            new_name='disease_details',
        ),
        migrations.RenameField(
            model_name='physicalexamination',
            old_name='remarks',
            new_name='other_physical_details',
        ),
        migrations.RenameField(
            model_name='surgicalhistory',
            old_name='details',
            new_name='surgery_details',
        ),
        migrations.RenameField(
            model_name='treatmentantidiabetic',
            old_name='others',
            new_name='others_treatments',
        ),
        migrations.RenameField(
            model_name='treatmentantihypertensive',
            old_name='details',
            new_name='treatment_details',
        ),
        migrations.RenameField(
            model_name='treatmentothers',
            old_name='details',
            new_name='other_treatment_details',
        ),
    ]