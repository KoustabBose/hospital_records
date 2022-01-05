from django.db.models import fields
#from hospital_records.settings import get_patient_id
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.template.response import TemplateResponse,SimpleTemplateResponse
import datetime
import math

# Create your views here.
def index(request):
	data = {
		'search_form' : SearchBar(),
		'transaction_details' : TransactionDetailsForm(),
		'personal_details' : PersonalDetailsForm(),
		'family_history' : FamilyHistoryForm(),
		'medical_history' : MedicalHistoryFormSet(),
		'surgical_history' : SurgicalHistoryForm(),
		'diabetes_history' : DiabetesHistoryForm(),
	}
	return render(request,"index.html",data)

def search(request):
	if request.method == "POST":
		data = request.POST
		#print(data)
		searchForm = SearchBar(data)
		if searchForm.is_valid():
			search = searchForm.cleaned_data
			#print(search['search_type'])
			#print(search['search_str'])
		if search['search_type'] == "M":
			queryset = PersonalDetails.objects.filter(MR_no = search['search_str'])
		if search['search_type'] == "F":
			queryset = PersonalDetails.objects.filter(file_no = search['search_str'])
		if search['search_type'] == "N":
			queryset = PersonalDetails.objects.filter(name = search['search_str'])
		
		pid = queryset.values()[0]['patient_id']
		transaction_data = TransactionDetails.objects.filter(patient_id = pid)
		data = {
			'search_form' : SearchBar(),
			'patient_id' :pid,
			'name' : queryset.values()[0]['name'],
			'age' : math.floor((datetime.date.today() - queryset.values()[0]['registration_date']).days/365.2425) + queryset.values()[0]['age'],
			'sex' : queryset.values()[0]['sex'],
		}
		for i in transaction_data.values():
			if i['ttype'] == 'history':
				temp = {}
				temp.setdefault('history',{}).update({'patient_id' : pid})
				data.update(temp)
			if i['ttype'] == 'reports':
				temp = {}
				if 'reports' in data.keys():
					data['reports']['date'].append(i['date'])
				else:
					temp.setdefault('reports',{}).update({'date' : [i['date']],'patient_id' : pid})
					data.update(temp)
			if i['ttype'] == 'treatment':
				temp = {}
				if 'treatment' in data.keys():
					data['treatment']['date'].append(i['date'])
				else:
					temp.setdefault('treatment',{}).update({'date' : [i['date']],'patient_id' : pid})
					data.update(temp)
		#transaction_details = get_object_or_404(TransactionDetails,queryset=queryset)
		##print(transaction_details)
		#print(data)
		return render(request,'search_result.html',data)

def login_page(request):
	return HttpResponse("Login")

def insertnew(request):
	if request.method == "GET":
		return render(request,"index.html")

	if request.method == "POST":
		data = request.POST
		pid = get_patient_id()
		print(data)

		transaction_details_form = TransactionDetailsForm(data)
		personal_details_form = PersonalDetailsForm(data)
		family_history_form =  FamilyHistoryForm(data)
		medical_history_form =  MedicalHistoryFormSet(data)
		surgical_history_form =  SurgicalHistoryForm(data)
		diabetes_history_form =  DiabetesHistoryForm(data)
		if transaction_details_form.is_valid():
			transaction_details=transaction_details_form.save(commit=False)
			transaction_details.ttype = 'history'
		else:
			return render(request,'data_error.html',{'message' : 'Error in Transaction Details Data:' + str(transaction_details_form.errors)})
		if personal_details_form.is_valid():
			personal_details = personal_details_form.save(commit=False)
			personal_details.patient_id = pid
			transaction_details.patient_id=personal_details
			personal_details.registration_date = transaction_details.date
			
		else:
			return render(request,'data_error.html',{'message' : 'Error in Personal Details Data:' + str(personal_details_form.errors)})
		if family_history_form.is_valid():
			family_history = family_history_form.save(commit=False)
			family_history.patient_id=personal_details
			family_history.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Family History Data:' + str(family_history_form.errors)})
		if medical_history_form.is_valid():
			medical_history_list = []
			for form in medical_history_form:
				medical_history = form.save(commit=False)
				medical_history.patient_id=personal_details
				medical_history.entry_date = transaction_details.date
				medical_history_list.append(medical_history)
		else:
			return render(request,'data_error.html',{'message' : 'Error in Medical History Data:' + str(medical_history_form.errors)})
		if surgical_history_form.is_valid():
			surgical_history = surgical_history_form.save(commit=False)
			surgical_history.patient_id=personal_details
			surgical_history.entry_date = transaction_details.date
			#print(surgical_history.surgery_details)
		else:
			return render(request,'data_error.html',{'message' : 'Error in Surgical History Data:' + str(surgical_history_form.errors)})
		if diabetes_history_form.is_valid():
			diabetes_history = diabetes_history_form.save(commit=False)
			diabetes_history.patient_id=personal_details
			diabetes_history.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Diabetes History Data:' + str(diabetes_history_form.errors)})


		personal_details.save()
		transaction_details.save()
		family_history.save()
		for x in medical_history_list:
			x.save()
		surgical_history.save()
		diabetes_history.save()

		return render(request,'data_success.html',{'message' : 'Data Submitted Successfully'})

def insertreports(request):
	if request.method == "GET":
		in_data = request.GET.get('patient_id')
		queryset = PersonalDetails.objects.filter(pk=in_data)
		name = queryset.values()[0]['name']
		age = queryset.values()[0]['age']
		sex = queryset.values()[0]['sex']
		data = {
			'name': name,
			'age' : age,
			'sex' : sex,
			'patient_id' : in_data,
			'search_form' : SearchBar(),
			'transaction_details' : TransactionDetailsForm(),
			'physical_exam' : PhysicalExaminationForm(),
			'blood_sugar' : InvestigationBloodSugarForm(),
			'renal' : InvestigationRenalForm(),
			'blood_lipid' : InvestigationBloodLipidsForm(),
			'liver_func' : InvestigationLiverFunctionForm(),
			'haemogram' : InvestigationHaemogramForm(),
			'blood_others' : InvestigationBloodOthersForm(),
			'urine' : InvestigationUrineForm(),
			'others' : InvestigationOthersForm(),
		}

		return render(request,'insertreports.html',data)

	if request.method == "POST":
		data = request.POST
		pid = data.get('patient_id')
		personal_details = PersonalDetails.objects.get(pk=pid)
		transaction_details_form = TransactionDetailsForm(data)
		personal_details_form = PersonalDetailsForm(data)
		physical_exam_form =  PhysicalExaminationForm(data)
		blood_sugar_form =  InvestigationBloodSugarForm(data)
		renal_form =  InvestigationRenalForm(data)
		blood_lipid_form =  InvestigationBloodLipidsForm(data)
		liver_func_form =  InvestigationLiverFunctionForm(data)
		haemogram_form =  InvestigationHaemogramForm(data)
		blood_others_form =  InvestigationBloodOthersForm(data)
		urine_form =  InvestigationUrineForm(data)
		others_form =  InvestigationOthersForm(data)
		if transaction_details_form.is_valid():
			transaction_details=transaction_details_form.save(commit=False)
			transaction_details.ttype = 'reports'
			transaction_details.patient_id=personal_details
		else:
			return render(request,'data_error.html',{'message' : 'Error in Transaction Details Data:' + str(transaction_details_form.errors)})

		if physical_exam_form.is_valid():
			physical_exam = physical_exam_form.save(commit=False)
			physical_exam.patient_id=personal_details
			physical_exam.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Physical Examination Data:' + str(personal_details_form.errors)})
		if blood_sugar_form.is_valid():
			blood_sugar = blood_sugar_form.save(commit=False)
			blood_sugar.patient_id=personal_details
			blood_sugar.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Blood Sugar Data:' + str(personal_details_form.errors)})
		if renal_form.is_valid():
			renal = renal_form.save(commit=False)
			renal.patient_id=personal_details
			renal.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Renal Data:' + str(personal_details_form.errors)})
		if blood_lipid_form.is_valid():
			blood_lipid = blood_lipid_form.save(commit=False)
			blood_lipid.patient_id=personal_details
			blood_lipid.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Lipid Data:' + str(personal_details_form.errors)})
		if liver_func_form.is_valid():
			liver_func = liver_func_form.save(commit=False)
			liver_func.patient_id=personal_details
			liver_func.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Liver Function Data:' + str(personal_details_form.errors)})
		if haemogram_form.is_valid():
			haemogram = haemogram_form.save(commit=False)
			haemogram.patient_id=personal_details
			haemogram.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Haemogram Data:' + str(personal_details_form.errors)})
		if blood_others_form.is_valid():
			blood_others = blood_others_form.save(commit=False)
			blood_others.patient_id=personal_details
			blood_others.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Other Blood Data:' + str(personal_details_form.errors)})
		if urine_form.is_valid():
			urine = urine_form.save(commit=False)
			urine.patient_id=personal_details
			urine.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Urine Data:' + str(personal_details_form.errors)})
		if others_form.is_valid():
			others = others_form.save(commit=False)
			others.patient_id=personal_details
			others.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Other Investigation Data:' + str(personal_details_form.errors)})

		transaction_details.save()
		blood_lipid.save()
		blood_others.save()
		blood_sugar.save()
		haemogram.save()
		liver_func.save()
		others.save()
		physical_exam.save()
		renal.save()
		urine.save()

		return render(request,'data_success.html',{'message' : 'Data Submitted Successfully'})

def inserttreatment(request):
	if request.method == "GET":
		in_data = request.GET.get('patient_id')
		queryset = PersonalDetails.objects.filter(pk=in_data)
		name = queryset.values()[0]['name']
		age = queryset.values()[0]['age']
		sex = queryset.values()[0]['sex']
		data = {
			'name': name,
			'age' : age,
			'sex' : sex,
			'patient_id' : in_data,
			'search_form' : SearchBar(),
			'transaction_details' : TransactionDetailsForm(),
			'diagnosis' : DiagnosisForm(),
			'treat_diabetes' : TreatmentAntiDiabeticForm(),
			'treat_HT' : TreatmentAntiHypertensiveForm(),
			'treat_others' : TreatmentOthersForm(),
		}

		return render(request,'inserttreatment.html',data)

	if request.method == "POST":
		data = request.POST
		print(data)
		pid = data.get('patient_id')
		personal_details = PersonalDetails.objects.get(pk=pid)
		transaction_details_form = TransactionDetailsForm(data)
		diagnosis_form = DiagnosisForm(data)
		treat_diabetes_form =  TreatmentAntiDiabeticForm(data)
		treat_HT_form =  TreatmentAntiHypertensiveForm(data)
		treat_others_form =  TreatmentOthersForm(data)
		if transaction_details_form.is_valid():
			transaction_details=transaction_details_form.save(commit=False)
			transaction_details.ttype = 'treatment'
			transaction_details.patient_id=personal_details
		else:
			return render(request,'data_error.html',{'message' : 'Error in Transaction Details Data:' + str(transaction_details_form.errors)})

		if diagnosis_form.is_valid():
			diagnosis = diagnosis_form.save(commit=False)
			diagnosis.patient_id=personal_details
			diagnosis.entry_date = transaction_details.date

		if treat_diabetes_form.is_valid():
			treat_diabetes = treat_diabetes_form.save(commit=False)
			treat_diabetes.patient_id=personal_details
			treat_diabetes.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Diabetes Treatment Data:' + str(treat_diabetes_form.errors)})

		if treat_HT_form.is_valid():
			treat_HT = treat_HT_form.save(commit=False)
			treat_HT.patient_id=personal_details
			treat_HT.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Hypertension treatment Data:' + str(treat_HT_form.errors)})

		if treat_others_form.is_valid():
			treat_others = treat_others_form.save(commit=False)
			treat_others.patient_id=personal_details
			treat_others.entry_date = transaction_details.date
		else:
			return render(request,'data_error.html',{'message' : 'Error in Other treatment Data:' + str(treat_others_form.errors)})

		transaction_details.save()
		diagnosis.save()
		treat_HT.save()
		treat_diabetes.save()
		treat_others.save()
		return render(request,'data_success.html',{'message' : 'Data Submitted Successfully'})


def fetch_history(request):
	if request.method == "GET":
		pid = request.GET.get('patient_id')
		pk_instance = PersonalDetails.objects.get(pk=pid)
		personal_details = PersonalDetails.objects.filter(pk=pid)
		family_history = FamilyHistory.objects.filter(patient_id=pid)
		medical_history = MedicalHistory.objects.filter(patient_id=pid)
		surgical_history = SurgicalHistory.objects.filter(patient_id=pid)
		diabetes_history = DiabetesHistory.objects.filter(patient_id=pid)

		data = {
			'search_form' : SearchBar(),
			'personal_details' : personal_details.values('file_no','MR_no','name','age','sex','address','pincode','marital_status','religion','country','contact_no','email_id','consultant','registration_date'),
			'family_history' : family_history.values('diabetes'),
			'medical_history' : medical_history.values('disease','duration_in_years','disease_details'),
			'surgical_history' : surgical_history.values('surgery_details'),
			'diabetes_history' : diabetes_history.values('hypoglycemia','eye_complications','kidney_complications','heart_complications','foot_complications','nerve_complications','other_diabetic_complication'),
		}

		return render(request,'show_history.html',data)


def fetch_report(request):
	if request.method == "GET":
		pid = request.GET.get('patient_id')
		date = request.GET.get('date')
		pk_instance = PersonalDetails.objects.get(pk=pid)
		physical_exam = PhysicalExamination.objects.filter(patient_id=pid,entry_date=date)
		blood_sugar = InvestigationBloodSugar.objects.filter(patient_id=pid,entry_date=date)
		renal = InvestigationRenal.objects.filter(patient_id=pid,entry_date=date)
		blood_lipid = InvestigationBloodLipids.objects.filter(patient_id=pid,entry_date=date)
		liver_func = InvestigationLiverFunction.objects.filter(patient_id=pid,entry_date=date)
		haemogram = InvestigationHaemogram.objects.filter(patient_id=pid,entry_date=date)
		blood_others = InvestigationBloodOthers.objects.filter(patient_id=pid,entry_date=date)
		urine = InvestigationUrine.objects.filter(patient_id=pid,entry_date=date)
		others = InvestigationOthers.objects.filter(patient_id=pid,entry_date=date)

		data = {
			'search_form' : SearchBar(),
			'physical_exam' : physical_exam.values('height','weight','BMI','hip','waist','race','pulse_rate','systolic_BP','diastolic_BP','SPO2','random_blood_Sugar','smoking','alcohol','AntiHyperTensiveDrug','other_physical_details'),
			'blood_sugar' : blood_sugar.values('fasting','post_prandial','HbA1c','EGDR'),
			'renal' : renal.values('urea','creatinine','EGFR','CKD_stage'),
			'blood_lipid' : blood_lipid.values('total_cholestrol','triglyceride','HDL','LDL','VLDL','ASCVD_Score'),
			'liver_func' : liver_func.values('bilirubin_T','bilirubin_D','bilirubin_I','total_protein','albumin','globulin','AG_ratio','SGOT','SGPT','alkaline_phosphate','GGT','uric_acid','fibroscan'),
			'haemogram' : haemogram.values('haemoglobin','WBC','neutrophil','lymphocyte','monocyte','eosinophil','basophil','ESR','Platelets','PCV'),
			'blood_others' : blood_others.values('T3','T4','TSH','calcium','sodium','potassium','iron','ferritine','vitamin_D','vitamin_B12'),
			'urine' : urine.values('albumin','glucose','ketone','RBC','leukocytes','micro_albumin','urine_protein_24_hour','culture'),
			'others' : others.values('retina','chest_xray','ECG','USG','ECHO','Foot_Screening'),
		}

		return render(request,'show_reports.html',data)


def fetch_treatment(request):
	if request.method == "GET":
		pid = request.GET.get('patient_id')
		date = request.GET.get('date')
		pk_instance = PersonalDetails.objects.get(pk=pid)
		treat_diabetes = TreatmentAntiDiabetic.objects.filter(patient_id=pid,entry_date=date)
		treat_HT = TreatmentAntiHypertensive.objects.filter(patient_id=pid,entry_date=date)
		treat_others = TreatmentOthers.objects.filter(patient_id=pid,entry_date=date)

		data = {
			'search_form' : SearchBar(),
			'treat_diabetes' : treat_diabetes.values('sulfonylurea','metformin','SGLT2_inhibitor','DPP4_inhibitor','pioglitazone','insulin_bolus','insulin_basal','others_treatments'),
			'treat_HT' : treat_HT.values('treatment_details'),
			'treat_others' : treat_others.values('other_treatment_details'),
		}
	return render(request,'show_treatment.html',data)
	
	if request.method == "POST":
		return render(request,'data_error.html',{"message" : "Invalid Request"})


def advanced_search(request):
	if request.method == "GET":
		data = {'search_form' : SearchBar(),
				'advanced_search' : AdvancedSearchForm(),
		}
		return render(request,'advanced_search.html',data)

	if request.method == "POST":
		return render(request,'data_error.html',{'message' : 'Invalid Request'})

