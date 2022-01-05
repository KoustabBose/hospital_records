# Generated by Django 3.2.6 on 2021-08-28 06:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Unmarried', 'Unmarried'), ('Married', 'Married'), ('Other', 'Other')], max_length=10, null=True)),
                ('mobile_no', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, choices=[('AF', 'Afghanistan'), ('AX', 'Alandislands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'Americansamoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antiguaandbarbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosniaandherzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvetisland'), ('BR', 'Brazil'), ('IO', 'Britishindianoceanterritory'), ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkinafaso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Capeverde'), ('KY', 'Caymanislands'), ('CF', 'Centralafricanrepublic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmasisland'), ('CC', 'Cocos(keeling)islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Drcongo'), ('CK', 'Cookislands'), ('CR', 'Costarica'), ('CI', 'Ivorycoast'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominicanrepublic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'Elsalvador'), ('GQ', 'Equatorialguinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falklandislands(malvinas)'), ('FO', 'Faroeislands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'Frenchguiana'), ('PF', 'Frenchpolynesia'), ('TF', 'Frenchsouthernterritories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heardisland&mcdonaldislands'), ('VA', 'Holysee(vaticancitystate)'), ('HN', 'Honduras'), ('HK', 'Hongkong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isleofman'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Hashemitekingdomofjordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KR', 'Republicofkorea'), ('KR', 'Southkorea'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Republicoflithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Northmacedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshallislands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia,federatedstatesof'), ('MD', 'Republicofmoldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlandsantilles'), ('NC', 'Newcaledonia'), ('NZ', 'Newzealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolkisland'), ('MP', 'Northernmarianaislands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papuanewguinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puertorico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('BL', 'Saintbarthelemy'), ('SH', 'Sainthelena'), ('KN', 'Saintkittsandnevis'), ('LC', 'Saintlucia'), ('MF', 'Saintmartin'), ('PM', 'Saintpierreandmiquelon'), ('VC', 'Saintvincentandgrenadines'), ('WS', 'Samoa'), ('SM', 'Sanmarino'), ('ST', 'Saotomeandprincipe'), ('SA', 'Saudiarabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierraleone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomonislands'), ('SO', 'Somalia'), ('ZA', 'Southafrica'), ('GS', 'Southgeorgiaandsandwichisl.'), ('ES', 'Spain'), ('LK', 'Srilanka'), ('SD', 'Sudan'), ('SS', 'Southsudan'), ('SR', 'Suriname'), ('SJ', 'Svalbardandjanmayen'), ('SZ', 'Eswatini'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidadandtobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turksandcaicosislands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'Unitedarabemirates'), ('GB', 'Unitedkingdom'), ('US', 'Unitedstates'), ('UM', 'Unitedstatesoutlyingislands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('VG', 'Virginislands,british'), ('VI', 'Virginislands,u.s.'), ('WF', 'Wallisandfutuna'), ('EH', 'Westernsahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('patient_id', models.PositiveBigIntegerField(default=0, primary_key=True, serialize=False)),
                ('file_no', models.IntegerField(blank=True, null=True, unique=True)),
                ('MR_no', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Unmarried', 'Unmarried'), ('Married', 'Married'), ('Other', 'Other')], max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, choices=[('AF', 'Afghanistan'), ('AX', 'Alandislands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'Americansamoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antiguaandbarbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosniaandherzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvetisland'), ('BR', 'Brazil'), ('IO', 'Britishindianoceanterritory'), ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkinafaso'), ('BI', 'Burundi'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Capeverde'), ('KY', 'Caymanislands'), ('CF', 'Centralafricanrepublic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmasisland'), ('CC', 'Cocos(keeling)islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'), ('CD', 'Drcongo'), ('CK', 'Cookislands'), ('CR', 'Costarica'), ('CI', 'Ivorycoast'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominicanrepublic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'Elsalvador'), ('GQ', 'Equatorialguinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falklandislands(malvinas)'), ('FO', 'Faroeislands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'Frenchguiana'), ('PF', 'Frenchpolynesia'), ('TF', 'Frenchsouthernterritories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heardisland&mcdonaldislands'), ('VA', 'Holysee(vaticancitystate)'), ('HN', 'Honduras'), ('HK', 'Hongkong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isleofman'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Hashemitekingdomofjordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KR', 'Republicofkorea'), ('KR', 'Southkorea'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Republicoflithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Northmacedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshallislands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia,federatedstatesof'), ('MD', 'Republicofmoldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('AN', 'Netherlandsantilles'), ('NC', 'Newcaledonia'), ('NZ', 'Newzealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolkisland'), ('MP', 'Northernmarianaislands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papuanewguinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puertorico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('BL', 'Saintbarthelemy'), ('SH', 'Sainthelena'), ('KN', 'Saintkittsandnevis'), ('LC', 'Saintlucia'), ('MF', 'Saintmartin'), ('PM', 'Saintpierreandmiquelon'), ('VC', 'Saintvincentandgrenadines'), ('WS', 'Samoa'), ('SM', 'Sanmarino'), ('ST', 'Saotomeandprincipe'), ('SA', 'Saudiarabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierraleone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomonislands'), ('SO', 'Somalia'), ('ZA', 'Southafrica'), ('GS', 'Southgeorgiaandsandwichisl.'), ('ES', 'Spain'), ('LK', 'Srilanka'), ('SD', 'Sudan'), ('SS', 'Southsudan'), ('SR', 'Suriname'), ('SJ', 'Svalbardandjanmayen'), ('SZ', 'Eswatini'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidadandtobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turksandcaicosislands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'Unitedarabemirates'), ('GB', 'Unitedkingdom'), ('US', 'Unitedstates'), ('UM', 'Unitedstatesoutlyingislands'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('VG', 'Virginislands,british'), ('VI', 'Virginislands,u.s.'), ('WF', 'Wallisandfutuna'), ('EH', 'Westernsahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, null=True)),
                ('contact_no', models.IntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('consultant', models.CharField(choices=[('Dr. Ghansyam Goyal', 'Dr. Ghansyam Goyal')], default='Dr. Ghanshyam Goyal', max_length=200)),
                ('registration_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentOthers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentAntiHypertensive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentAntiDiabetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('sulfonylurea', models.TextField(blank=True, null=True)),
                ('metformin', models.TextField(blank=True, null=True)),
                ('SGLT2_inhibitor', models.TextField(blank=True, null=True)),
                ('DPP4_inhibitor', models.TextField(blank=True, null=True)),
                ('insulin_bolus', models.TextField(blank=True, null=True)),
                ('insulin_basal', models.TextField(blank=True, null=True)),
                ('others', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('ttype', models.CharField(choices=[('history', 'history'), ('reports', 'reports'), ('treatment', 'treatment')], default='history', max_length=50)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('details', models.TextField(blank=True, default='NA', null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('BMI', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hip', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('waist', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('race', models.CharField(blank=True, choices=[('black', 'black'), ('others', 'others')], default='others', max_length=10, null=True)),
                ('pulse_rate', models.IntegerField(blank=True, null=True)),
                ('systolic_BP', models.IntegerField(blank=True, null=True)),
                ('diastolic_BP', models.IntegerField(blank=True, null=True)),
                ('SPO2', models.IntegerField(blank=True, null=True)),
                ('random_blood_Sugar', models.IntegerField(blank=True, null=True)),
                ('smoking', models.BooleanField(blank=True, choices=[(1, 'Yes'), (0, 'No')], default=0, null=True)),
                ('alcohol', models.BooleanField(blank=True, choices=[(1, 'Yes'), (0, 'No')], default=0, null=True)),
                ('AntiHyperTensiveDrug', models.BooleanField(blank=True, choices=[(1, 'Yes'), (0, 'No')], default=0, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(choices=[('Heart Disease', 'Heart Disease'), ('Kidney Disease', 'Kidney Disease'), ('Liver Disease', 'Liver Disease'), ('Asthma/COPD', 'Asthma/COPD'), ('Hypertension', 'Hypertension'), ('Chronic Infections', 'Chronic Infections'), ('Other', 'Other')], max_length=50)),
                ('duration_in_years', models.IntegerField(blank=True, null=True)),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationUrine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('albumin', models.CharField(blank=True, max_length=50, null=True)),
                ('glucose', models.CharField(blank=True, max_length=50, null=True)),
                ('ketone', models.CharField(blank=True, max_length=50, null=True)),
                ('RBC', models.CharField(blank=True, max_length=50, null=True)),
                ('leukocytes', models.CharField(blank=True, max_length=50, null=True)),
                ('micro_albumin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('urine_protein_24_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('culture', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationRenal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('urea', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('creatinine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('EGFR', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('CKD_stage', models.IntegerField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationOthers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('retina', models.TextField(blank=True, null=True)),
                ('chest_xray', models.TextField(blank=True, null=True)),
                ('ECG', models.TextField(blank=True, null=True)),
                ('USG', models.TextField(blank=True, null=True)),
                ('ECHO', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationLiverFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('bilirubin_T', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bilirubin_D', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bilirubin_I', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('total_protein', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('albumin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('globulin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('AG_ratio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('SGOT', models.IntegerField(blank=True, null=True)),
                ('SGPT', models.IntegerField(blank=True, null=True)),
                ('alkaline_phosphate', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('GGT', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('uric_acid', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationHaemogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('haemoglobin', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('WBC', models.IntegerField(blank=True, null=True)),
                ('neutrophil', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('lymphocyte', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('monocyte', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('eosinophil', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('basophil', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('ESR', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Platelets', models.IntegerField(blank=True, null=True)),
                ('PCV', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationBloodSugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('fasting', models.IntegerField(blank=True, null=True)),
                ('post_prandial', models.IntegerField(blank=True, null=True)),
                ('HbA1c', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('EGDR', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationBloodOthers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('T3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('T4', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('TSH', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('calcium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('sodium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('potassium', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('iron', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('ferritine', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vitamin_D', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('vitamin_B12', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationBloodLipids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('total_cholestrol', models.IntegerField(blank=True, null=True)),
                ('triglyceride', models.IntegerField(blank=True, null=True)),
                ('HDL', models.IntegerField(blank=True, null=True)),
                ('LDL', models.IntegerField(blank=True, null=True)),
                ('VLDL', models.IntegerField(blank=True, null=True)),
                ('ASCVD_Score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diabetes', models.BooleanField(blank=True, choices=[(1, 'Yes'), (0, 'No')], default=0, null=True)),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
        migrations.CreateModel(
            name='DiabetesHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(blank=True, null=True)),
                ('hypoglycemia', models.BooleanField()),
                ('eye_complications', models.BooleanField()),
                ('kidney_complications', models.BooleanField()),
                ('heart_complications', models.BooleanField()),
                ('foot_complications', models.BooleanField()),
                ('nerve_complications', models.BooleanField()),
                ('details', models.TextField(blank=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetic_clinic.personaldetails')),
            ],
        ),
    ]
