from django import forms
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.forms import ModelForm,Form
from betterforms.multiform import MultiModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import ChoiceWidget, HiddenInput, RadioSelect, SelectDateWidget
from .models import *
from .choices import *
from collections import OrderedDict
from django.forms import modelformset_factory,formset_factory


class SearchBar(forms.Form):
    search_str = forms.CharField(label="Search Patients",max_length=100)
    search_type = forms.ChoiceField(label="Search By",choices=CHOICES_SEARCH,widget=forms.RadioSelect,initial="M")    

class TransactionDetailsForm(ModelForm):
    class Meta:
        model = TransactionDetails
        exclude = ['patient_id','ttype']
        widgets = {
            "date" : SelectDateWidget(years=[2000+i for i in range(100)]),
        }

class DoctorDetailsForm(ModelForm):
    class Meta:
        model = DoctorsDetails
        exclude = ['id']
        widgets = {
            "DOB" : SelectDateWidget
        }

class PatientForm(forms.Form):
    patient_id = PositiveBigIntegerField,
    name = CharField(max_length=100)

class PersonalDetailsForm(ModelForm):
    class Meta:
        model = PersonalDetails
        exclude = ['patient_id']
        widgets = {
            "DOB" : SelectDateWidget(years=[1900+i for i in range(200)]),
            "registration_date" : SelectDateWidget(years=[2000+i for i in range(100)])
        }

class FamilyHistoryForm(ModelForm):
    class Meta:
        model = FamilyHistory
        exclude = ['patient_id','entry_date']
        widgets = {
            "diabetes" : RadioSelect,
        }

class MedicalHistoryForm(ModelForm):
    class Meta:
        model = MedicalHistory
        exclude = ['patient_id','entry_date']

MedicalHistoryFormSet = formset_factory(MedicalHistoryForm,extra=1,max_num=10)

class SurgicalHistoryForm(ModelForm):
    class Meta:
        model =SurgicalHistory
        exclude = ['patient_id','entry_date']

class DiabetesHistoryForm(ModelForm):
    class Meta:
        model = DiabetesHistory
        exclude = ['patient_id','entry_date']

class PhysicalExaminationForm(ModelForm):
    class Meta:
        model = PhysicalExamination
        exclude = ['patient_id','entry_date']
        widgets = {
            'smoking' : RadioSelect,
            'alcohol' : RadioSelect,
        }

class InvestigationBloodSugarForm(ModelForm):
    class Meta:
        model = InvestigationBloodSugar
        exclude = ['patient_id','entry_date']
        

class InvestigationRenalForm(ModelForm):
    class Meta:
        model = InvestigationRenal
        exclude = ['patient_id','entry_date']
        

class InvestigationBloodLipidsForm(ModelForm):
    class Meta:
        model = InvestigationBloodLipids
        exclude = ['patient_id','entry_date']
        

class InvestigationLiverFunctionForm(ModelForm):
    class Meta:
        model = InvestigationLiverFunction
        exclude = ['patient_id','entry_date']
        

class InvestigationHaemogramForm(ModelForm):
    class Meta:
        model = InvestigationHaemogram
        exclude = ['patient_id','entry_date']
        

class InvestigationBloodOthersForm(ModelForm):
    class Meta:
        model = InvestigationBloodOthers
        exclude = ['patient_id','entry_date']
        

class InvestigationUrineForm(ModelForm):
    class Meta:
        model = InvestigationUrine
        exclude = ['patient_id','entry_date']
        

class InvestigationOthersForm(ModelForm):
    class Meta:
        model = InvestigationOthers
        exclude = ['patient_id','entry_date']
        

class TreatmentAntiDiabeticForm(ModelForm):
    class Meta:
        model = TreatmentAntiDiabetic
        exclude = ['patient_id','entry_date']
        

class TreatmentAntiHypertensiveForm(ModelForm):
    class Meta:
        model = TreatmentAntiHypertensive
        exclude = ['patient_id','entry_date']
        

class TreatmentOthersForm(ModelForm):
    class Meta:
        model = TreatmentOthers
        exclude = ['patient_id','entry_date']

class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        exclude = ['patient_id','entry_date']
        
class AdvancedSearchForm(Form):
    search = forms.ChoiceField(choices=CHOICES_FIELDS,label="Search")
    value1 = forms.CharField(max_length=10,label="Min Value")
    value2 = forms.CharField(max_length=10,label="Max value")
