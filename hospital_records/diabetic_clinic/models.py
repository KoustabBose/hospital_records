from hospital_records.settings import DEFAULT_AUTO_FIELD
from django.db import models
from django.db.models.base import Model
from django.forms import widgets
from django.utils.formats import date_format
import datetime
from .choices import *
from django.utils import timezone


# Create your models here.

class DoctorsDetails(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=100)
	DOB = models.DateField(null=True,blank=True)
	age = models.IntegerField(null=True,blank=True)
	sex = models.CharField(max_length=10,choices=CHOICES_SEX)
	address = models.CharField(max_length=200,null=True,blank=True)
	pincode = models.IntegerField(null=True,blank=True)
	marital_status = models.CharField(max_length=10,null=True,blank=True,choices=CHOICES_MARITAL)
	mobile_no = models.BigIntegerField(null=True,blank=True)
	country = models.CharField(max_length=2,null=True,blank=True,choices=CHOICES_COUNTRY)

class PersonalDetails(models.Model):
	patient_id = models.PositiveBigIntegerField(primary_key=True,default=0)
	file_no = models.IntegerField(null=True,blank=True,unique=True)
	MR_no = models.IntegerField(null=True,blank=True,unique=True)
	name = models.CharField(max_length=100)
	age = models.IntegerField(null=True,blank=True,help_text='Years')
	sex = models.CharField(max_length=10,choices=CHOICES_SEX)
	address = models.CharField(max_length=200,null=True,blank=True)
	pincode = models.IntegerField(null=True,blank=True)
	marital_status = models.CharField(max_length=10,null=True,blank=True,choices=CHOICES_MARITAL)
	religion = models.CharField(max_length=20,null=True,blank=True)
	country = models.CharField(max_length=2,choices=CHOICES_COUNTRY,null=True,blank=True)
	contact_no = models.BigIntegerField(null=True,blank=True)
	email_id = models.EmailField(null=True,blank=True)
	#consultant = models.IntegerField(choices=DoctorsDetails.objects.all().values("id","name"))
	consultant = models.CharField(max_length=200,choices=CHOICES_DOCTORS,default='Dr. Ghanshyam Goyal')
	registration_date = models.DateField(null=True,blank=True)


class TransactionDetails(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)
	ttype = models.CharField(max_length=50,choices=CHOICES_TRANSACTION,default='history')

class FamilyHistory(models.Model):
	patient_id = models.ForeignKey(PersonalDetails,on_delete=models.CASCADE)
	diabetes = models.BooleanField(null=True,blank=True,default=0,choices=CHOICE_BOOL)
	entry_date = models.DateField(null=True,blank=True)

class MedicalHistory(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	disease = models.CharField(max_length=50,choices=CHOICES_DISEASE)
	duration_in_years = models.IntegerField(null=True,blank=True)
	entry_date = models.DateField(null=True,blank=True)
	disease_details = models.TextField(null=True,blank=True)

class SurgicalHistory(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	surgery_details = models.TextField(null=True,blank=True,default="NA")

class DiabetesHistory(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	hypoglycemia = models.BooleanField()
	eye_complications = models.BooleanField()
	kidney_complications = models.BooleanField()
	heart_complications = models.BooleanField()
	foot_complications = models.BooleanField()
	nerve_complications = models.BooleanField()
	other_diabetic_complication = models.TextField(blank=True)

class PhysicalExamination(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	height = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='cm')
	weight = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='kg')
	BMI = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='kg/m^2')
	hip = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='cm')
	waist = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='cm')
	race = models.CharField(max_length=10,null=True,blank=True,choices=CHOICES_RACE,default="others")
	pulse_rate = models.IntegerField(null=True,blank=True,help_text='bpm')
	systolic_BP = models.IntegerField(null=True,blank=True,help_text='mmHg')
	diastolic_BP = models.IntegerField(null=True,blank=True,help_text='mmHg')
	SPO2 = models.IntegerField(null=True,blank=True,help_text='%')
	random_blood_Sugar = models.IntegerField(null=True,blank=True,help_text='mm/dl')
	smoking = models.BooleanField(null=True,blank=True,default=0,choices=CHOICE_BOOL)
	alcohol = models.BooleanField(null=True,blank=True,default=0,choices=CHOICE_BOOL)
	AntiHyperTensiveDrug = models.BooleanField(null=True,blank=True,default=0,choices=CHOICE_BOOL)
	other_physical_details = models.TextField(null=True,blank=True)

class InvestigationBloodSugar(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	fasting = models.IntegerField(null=True,blank=True,help_text='mm/dl')
	post_prandial = models.IntegerField(null=True,blank=True,help_text='mm/dl')
	HbA1c = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True,help_text='%')
	EGDR = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)

class InvestigationRenal(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	urea = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	creatinine = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	EGFR = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	CKD_stage = models.CharField(null=True,blank=True,max_length=10)
	

class InvestigationBloodLipids(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	total_cholestrol = models.IntegerField(null=True,blank=True)
	triglyceride = models.IntegerField(null=True,blank=True)
	HDL = models.IntegerField(null=True,blank=True)
	LDL = models.IntegerField(null=True,blank=True)
	VLDL = models.IntegerField(null=True,blank=True)
	ASCVD_Score = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)

class InvestigationLiverFunction(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	bilirubin_T = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	bilirubin_D = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	bilirubin_I = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	total_protein = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	albumin = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	globulin = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	AG_ratio = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	SGOT = models.IntegerField(null=True,blank=True)
	SGPT = models.IntegerField(null=True,blank=True)
	alkaline_phosphate = models.DecimalField(max_digits=6,decimal_places=2 ,null=True,blank=True)
	GGT = models.DecimalField(max_digits=6,decimal_places=2 ,null=True,blank=True)
	uric_acid = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	fibroscan = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)

class InvestigationHaemogram(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	haemoglobin = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	WBC = models.IntegerField(null=True,blank=True)
	neutrophil = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	lymphocyte = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	monocyte = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	eosinophil = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	basophil = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	ESR = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	Platelets = models.IntegerField(null=True,blank=True)
	PCV = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)

class InvestigationBloodOthers(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	T3 = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	T4 = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	TSH = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	calcium = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	sodium = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	potassium = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	iron = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	ferritine = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	vitamin_D = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	vitamin_B12 = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)

class InvestigationUrine(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	albumin = models.CharField(max_length=50,null=True,blank=True)
	glucose = models.CharField(max_length=50,null=True,blank=True)
	ketone = models.CharField(max_length=50,null=True,blank=True)
	RBC = models.CharField(max_length=50,null=True,blank=True)
	leukocytes = models.CharField(max_length=50,null=True,blank=True)
	micro_albumin = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	urine_protein_24_hour = models.DecimalField(max_digits=5,decimal_places=2 ,null=True,blank=True)
	culture = models.TextField(null=True,blank=True)

class InvestigationOthers(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	retina = models.TextField(null=True,blank=True)
	chest_xray = models.TextField(null=True,blank=True)
	ECG = models.TextField(null=True,blank=True)
	USG = models.TextField(null=True,blank=True)
	ECHO = models.TextField(null=True,blank=True)
	Foot_Screening = models.TextField(null=True,blank=True)

class TreatmentAntiDiabetic(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	sulfonylurea = models.TextField(null=True,blank=True)
	metformin = models.TextField(null=True,blank=True)
	SGLT2_inhibitor = models.TextField(null=True,blank=True)
	DPP4_inhibitor = models.TextField(null=True,blank=True)
	pioglitazone = models.TextField(null=True,blank=True)
	insulin_bolus = models.TextField(null=True,blank=True)
	insulin_basal = models.TextField(null=True,blank=True)
	others_treatments = models.TextField(null=True,blank=True)

class TreatmentAntiHypertensive(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	treatment_details = models.TextField(null=True,blank=True)

class TreatmentOthers(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	other_treatment_details = models.TextField(null=True,blank=True)

class Diagnosis(models.Model):
	patient_id = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
	entry_date = models.DateField(null=True,blank=True)
	diagnosis = models.TextField(null=True,blank=True)
