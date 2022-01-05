CHOICE_BOOL = [(1,"Yes"),(0,"No")]

CHOICES_DOCTORS = [('Dr. Ghansyam Goyal','Dr. Ghansyam Goyal'),]

CHOICES_RACE = [('black','black'),('others','others'),]

CHOICES_TRANSACTION = [
("history","history"),
("reports","reports"),
("treatment","treatment")
]

CHOICES_DISEASE = [
        ("Diabetes","Diabetes"),
        ("Heart Disease","Heart Disease"),
        ("Kidney Disease","Kidney Disease"),
        ("Liver Disease","Liver Disease"),
        ("Asthma/COPD","Asthma/COPD"),
        ("Hypertension","Hypertension"),
        ("Chronic Infections","Chronic Infections"),
        ("Other","Other")
    ]

CHOICES_SEARCH = [("M","MR No."),("F","File No."),("N","Name")]
SEARCH_TYPE = {"M" : "MR_no","F" : "file_no","N" : "name"}

CHOICES_SEX = [
	("M","Male"),
	("F","Female"),
	("O","Other")
]

CHOICES_MARITAL = [
	("Unmarried","Unmarried"),
	("Married","Married"),
	("Other","Other")
]

CHOICES_FIELDS = [
	('','--'),
	('BMI',"BMI"),
	('systolic_BP','Systolic BP'),
	('diastolic_BP','Diastolic BP'),
	('SPO2','SPO2'),
	('fasting','Fasting Blood Sugar'),
	('post_prandial','PP Blood Sugar'),
	('HbA1c','HbA1c'),
	('EGDR','EGDR'),
	('urea','Urea'),
	('creatinine','Creatinine'),
	('EGFR','EGFR'),
	('ckd_stage','CKD Stage'),
]
CHOICES_FIELDS_MODEL = {
	'BMI' : ('PhysicalExamination','BMI'),
	'systolic_BP' : ('PhysicalExamination','systolic_BP'),
	'diastolic_BP' : ('PhysicalExamination','diastolic_BP'),
	'SPO2' : ('PhysicalExamination','SPO2'),
	'fasting' : ('InvestigationBloodSugar','fasting'),
	'post_prandial' : ('InvestigationBloodSugar','post_prandial'),
	'HbA1c' : ('InvestigationBloodSugar','HbA1c'),
	'EGDR' : ('InvestigationBloodSugar','EGDR'),
	'urea' : ('InvestigationRenal','urea'),
	'creatinine' : ('InvestigationRenal','creatinine'),
	'EGFR' : ('InvestigationRenal','EGFR'),
	'EGDR' : ('InvestigationRenal','EGDR'),
}

CHOICES_COUNTRY= [
	('AF', 'Afghanistan'),
	('AX', 'Alandislands'),
	('AL', 'Albania'),
	('DZ', 'Algeria'),
	('AS', 'Americansamoa'),
	('AD', 'Andorra'),
	('AO', 'Angola'),
	('AI', 'Anguilla'),
	('AQ', 'Antarctica'),
	('AG', 'Antiguaandbarbuda'),
	('AR', 'Argentina'),
	('AM', 'Armenia'),
	('AW', 'Aruba'),
	('AU', 'Australia'),
	('AT', 'Austria'),
	('AZ', 'Azerbaijan'),
	('BS', 'Bahamas'),
	('BH', 'Bahrain'),
	('BD', 'Bangladesh'),
	('BB', 'Barbados'),
	('BY', 'Belarus'),
	('BE', 'Belgium'),
	('BZ', 'Belize'),
	('BJ', 'Benin'),
	('BM', 'Bermuda'),
	('BT', 'Bhutan'),
	('BO', 'Bolivia'),
	('BA', 'Bosniaandherzegovina'),
	('BW', 'Botswana'),
	('BV', 'Bouvetisland'),
	('BR', 'Brazil'),
	('IO', 'Britishindianoceanterritory'),
	('BN', 'Brunei'),
	('BG', 'Bulgaria'),
	('BF', 'Burkinafaso'),
	('BI', 'Burundi'),
	('KH', 'Cambodia'),
	('CM', 'Cameroon'),
	('CA', 'Canada'),
	('CV', 'Capeverde'),
	('KY', 'Caymanislands'),
	('CF', 'Centralafricanrepublic'),
	('TD', 'Chad'),
	('CL', 'Chile'),
	('CN', 'China'),
	('CX', 'Christmasisland'),
	('CC', 'Cocos(keeling)islands'),
	('CO', 'Colombia'),
	('KM', 'Comoros'),
	('CG', 'Congo'),
	('CD', 'Drcongo'),
	('CK', 'Cookislands'),
	('CR', 'Costarica'),
	('CI', 'Ivorycoast'),
	('HR', 'Croatia'),
	('CU', 'Cuba'),
	('CY', 'Cyprus'),
	('CZ', 'Czechia'),
	('DK', 'Denmark'),
	('DJ', 'Djibouti'),
	('DM', 'Dominica'),
	('DO', 'Dominicanrepublic'),
	('EC', 'Ecuador'),
	('EG', 'Egypt'),
	('SV', 'Elsalvador'),
	('GQ', 'Equatorialguinea'),
	('ER', 'Eritrea'),
	('EE', 'Estonia'),
	('ET', 'Ethiopia'),
	('FK', 'Falklandislands(malvinas)'),
	('FO', 'Faroeislands'),
	('FJ', 'Fiji'),
	('FI', 'Finland'),
	('FR', 'France'),
	('GF', 'Frenchguiana'),
	('PF', 'Frenchpolynesia'),
	('TF', 'Frenchsouthernterritories'),
	('GA', 'Gabon'),
	('GM', 'Gambia'),
	('GE', 'Georgia'),
	('DE', 'Germany'),
	('GH', 'Ghana'),
	('GI', 'Gibraltar'),
	('GR', 'Greece'),
	('GL', 'Greenland'),
	('GD', 'Grenada'),
	('GP', 'Guadeloupe'),
	('GU', 'Guam'),
	('GT', 'Guatemala'),
	('GG', 'Guernsey'),
	('GN', 'Guinea'),
	('GW', 'Guinea-bissau'),
	('GY', 'Guyana'),
	('HT', 'Haiti'),
	('HM', 'Heardisland&mcdonaldislands'),
	('VA', 'Holysee(vaticancitystate)'),
	('HN', 'Honduras'),
	('HK', 'Hongkong'),
	('HU', 'Hungary'),
	('IS', 'Iceland'),
	('IN', 'India'),
	('ID', 'Indonesia'),
	('IR', 'Iran'),
	('IQ', 'Iraq'),
	('IE', 'Ireland'),
	('IM', 'Isleofman'),
	('IL', 'Israel'),
	('IT', 'Italy'),
	('JM', 'Jamaica'),
	('JP', 'Japan'),
	('JE', 'Jersey'),
	('JO', 'Hashemitekingdomofjordan'),
	('KZ', 'Kazakhstan'),
	('KE', 'Kenya'),
	('KI', 'Kiribati'),
	('KR', 'Republicofkorea'),
	('KR', 'Southkorea'),
	('KW', 'Kuwait'),
	('KG', 'Kyrgyzstan'),
	('LA', 'Laos'),
	('LV', 'Latvia'),
	('LB', 'Lebanon'),
	('LS', 'Lesotho'),
	('LR', 'Liberia'),
	('LY', 'Libya'),
	('LI', 'Liechtenstein'),
	('LT', 'Republicoflithuania'),
	('LU', 'Luxembourg'),
	('MO', 'Macao'),
	('MK', 'Northmacedonia'),
	('MG', 'Madagascar'),
	('MW', 'Malawi'),
	('MY', 'Malaysia'),
	('MV', 'Maldives'),
	('ML', 'Mali'),
	('MT', 'Malta'),
	('MH', 'Marshallislands'),
	('MQ', 'Martinique'),
	('MR', 'Mauritania'),
	('MU', 'Mauritius'),
	('YT', 'Mayotte'),
	('MX', 'Mexico'),
	('FM', 'Micronesia,federatedstatesof'),
	('MD', 'Republicofmoldova'),
	('MC', 'Monaco'),
	('MN', 'Mongolia'),
	('ME', 'Montenegro'),
	('MS', 'Montserrat'),
	('MA', 'Morocco'),
	('MZ', 'Mozambique'),
	('MM', 'Myanmar'),
	('NA', 'Namibia'),
	('NR', 'Nauru'),
	('NP', 'Nepal'),
	('NL', 'Netherlands'),
	('AN', 'Netherlandsantilles'),
	('NC', 'Newcaledonia'),
	('NZ', 'Newzealand'),
	('NI', 'Nicaragua'),
	('NE', 'Niger'),
	('NG', 'Nigeria'),
	('NU', 'Niue'),
	('NF', 'Norfolkisland'),
	('MP', 'Northernmarianaislands'),
	('NO', 'Norway'),
	('OM', 'Oman'),
	('PK', 'Pakistan'),
	('PW', 'Palau'),
	('PS', 'Palestine'),
	('PA', 'Panama'),
	('PG', 'Papuanewguinea'),
	('PY', 'Paraguay'),
	('PE', 'Peru'),
	('PH', 'Philippines'),
	('PN', 'Pitcairn'),
	('PL', 'Poland'),
	('PT', 'Portugal'),
	('PR', 'Puertorico'),
	('QA', 'Qatar'),
	('RE', 'Réunion'),
	('RO', 'Romania'),
	('RU', 'Russia'),
	('RW', 'Rwanda'),
	('BL', 'Saintbarthelemy'),
	('SH', 'Sainthelena'),
	('KN', 'Saintkittsandnevis'),
	('LC', 'Saintlucia'),
	('MF', 'Saintmartin'),
	('PM', 'Saintpierreandmiquelon'),
	('VC', 'Saintvincentandgrenadines'),
	('WS', 'Samoa'),
	('SM', 'Sanmarino'),
	('ST', 'Saotomeandprincipe'),
	('SA', 'Saudiarabia'),
	('SN', 'Senegal'),
	('RS', 'Serbia'),
	('SC', 'Seychelles'),
	('SL', 'Sierraleone'),
	('SG', 'Singapore'),
	('SK', 'Slovakia'),
	('SI', 'Slovenia'),
	('SB', 'Solomonislands'),
	('SO', 'Somalia'),
	('ZA', 'Southafrica'),
	('GS', 'Southgeorgiaandsandwichisl.'),
	('ES', 'Spain'),
	('LK', 'Srilanka'),
	('SD', 'Sudan'),
	('SS', 'Southsudan'),
	('SR', 'Suriname'),
	('SJ', 'Svalbardandjanmayen'),
	('SZ', 'Eswatini'),
	('SE', 'Sweden'),
	('CH', 'Switzerland'),
	('SY', 'Syria'),
	('TW', 'Taiwan'),
	('TJ', 'Tajikistan'),
	('TZ', 'Tanzania'),
	('TH', 'Thailand'),
	('TL', 'Timor-leste'),
	('TG', 'Togo'),
	('TK', 'Tokelau'),
	('TO', 'Tonga'),
	('TT', 'Trinidadandtobago'),
	('TN', 'Tunisia'),
	('TR', 'Turkey'),
	('TM', 'Turkmenistan'),
	('TC', 'Turksandcaicosislands'),
	('TV', 'Tuvalu'),
	('UG', 'Uganda'),
	('UA', 'Ukraine'),
	('AE', 'Unitedarabemirates'),
	('GB', 'Unitedkingdom'),
	('US', 'Unitedstates'),
	('UM', 'Unitedstatesoutlyingislands'),
	('UY', 'Uruguay'),
	('UZ', 'Uzbekistan'),
	('VU', 'Vanuatu'),
	('VE', 'Venezuela'),
	('VN', 'Vietnam'),
	('VG', 'Virginislands,british'),
	('VI', 'Virginislands,u.s.'),
	('WF', 'Wallisandfutuna'),
	('EH', 'Westernsahara'),
	('YE', 'Yemen'),
	('ZM', 'Zambia'),
	('ZW', 'Zimbabwe')
 ]