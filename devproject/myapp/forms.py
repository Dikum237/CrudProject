from django import forms  
from myapp.models import Employee  
import datetime
from django.utils import timezone
from django.forms.widgets import DateInput
from multiselectfield import MultiSelectField
from django.forms.widgets import SelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column




class EmployeeForm(forms.ModelForm):
    class Meta:  

        model = Employee  
        fields = ['Health_facility', 'worker_health_name', 'patient_name','patient_ID','Date_of_birth', 'Country','Region','District','sexe','Village', 
        'Phone_number','Occupation','Landmark','Contact_person','Contact_person_phone','detection_mode','classification','duration_illnes','use_traditional','any_treat',
        'treat_prev', 'Referred_by', 'Family_member','other_mode_detection','specify_any_treatment','duration_any','specify_for_previous','duration_for_previous',
        'number_family_close','relationship', 'other_referred','diagnosis','date_enregistrement', 'weigth','pregnant','HIV_status','TB_status','limitation_mov',
        'limitation_daily_act','category_lesion','Clinical_form','Location_lesion','no_lesions','diameter',] 

        SEXE_CHOICES = [('masculin', 'Male'), ('feminin', 'Female')]

        DETECTION_CHOICES=[('Active screening','Active screening'),('School survey', 'School survey '),('Referred','Referred'),('Passive','Passive'),('Other','Other')]

        CLASSIFICATION=[  ('New','New'), ('Recurrent','Recurent')]

        TRADITIONAL= [('Yes','Yes'), ('No','No')]
       
        REFERRED=[('self-referral','self-referral'),('Health worker','Health worker'), ('Village','Village'),('Traditional healer','Traditional healer'),
                     ('Family member','Family member'), ('Former patient','Former patient'), ('School Teacher', 'School Teacher'),('Other','Other')]
        
    
        Region_CHOICES = [('Adamaoua', 'Adamaoua'),('Centre','Centre'),('Est','Est'),('Extrême Nord','Extrême Nord'),('Littoral','Litoral'),
                             ('Nord','Nord'),('Nord Ouest','Nord ouest'),('Ouest','Ouest'),('Sud','Sud'),('Sud Ouest','Sud Ouest')]

        DISTRICT_CHOICES = [('Bankim','Bankim'),('Banyo','Banyo'),('Dang','Dang'),('Tibati','Tibati'),('Ngaoundere Rural','Ngaoundere Rural')]

        PREGNANT_LIST=[('Yes','Yes'), ('No','No'),('Unknown','Unknown')]

        INITIAL_CLINICAL=[('Positive','Positive'), ('Negative','Negative'),('Unknown','Unknown')]

        CLINICAL_FORMS=[('Nodule','Nodule'), ('Papule','Papule'),('Ulcere','Ulcere'),('Oedema','Oedema'),('Osteomyetlitis','Osteomyelitis')]

        LESION_LOCATION=[('Abdomen','Abdomen'),('Back','Back'),('Breast','Breast'),('Buttocks and perineum','Buttocks and perineum'),('Eye','Eye'),('Genitalia','Genitalia'),
                     ('Head and Neck','Head and Neck'), ('Inguinal/Groin','Inguinal/Groin'), ('Lower Limb','Lower Limb'),('Thorax','Thorax'),('Upper Limb','Upper Limb')
                     ]
        CATEGORY=[('Category I','Category I'),('Category II','Category II'),('Category III','Category III')]
        FAVORITE_COLORS_CHOICES = [
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
        ]
                
       

        widgets = { 
            
            'Health_facility': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'worker_health_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            'patient_name': forms.TextInput( attrs={ 'class': 'form-control' }),
            'patient_ID': forms.TextInput(attrs={'class':'form-control'}),
            'Date_of_birth': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            
            'Country': forms.TextInput(attrs={'class':'form-control'}),
          
            'Village': forms.TextInput(attrs={'class':'form-control'}),
            'Phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'Occupation': forms.TextInput(attrs={'class':'form-control'}),
            'Landmark': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact_person': forms.TextInput(attrs={'class':'form-control'}),
            'Contact_person_phone': forms.TextInput(attrs={'class':'form-control'}),
            'sexe':forms.Select(attrs={'class':'form-control'}),
            'Region':forms.Select(attrs={'class':'form-control'}),
            'District':forms.Select(attrs={'class':'form-control'}),
            'detection_mode':forms.Select(attrs={'class':'form-control'}),
            'classification':forms.Select(attrs={'class':'form-control'}),
            'duration_illnes':forms.TextInput(attrs={'class':'form-control'}),
            'use_traditional':forms.Select(attrs={'class':'form-control'}),
            'any_treat':forms.Select(attrs={'class':'form-control'}),
            'treat_prev':forms.Select(attrs={'class':'form-control'}),

            'Referred_by':forms.Select(attrs={'class':'form-control'}),

            'Family_member':forms.Select(attrs={'class':'form-control'}),
            'other_mode_detection':forms.TextInput(attrs={'class': 'form-control','placeholder':'Precise if Other detection mode'}),
            'specify_any_treatment':forms.TextInput(attrs={'class': 'form-control','placeholder':'Specify any treatment if Yes'}),
            'duration_any':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Duration in days'}),
            'specify_for_previous':forms.TextInput(attrs={'class': 'form-control','placeholder':'Specify any pevious treatment is Yes'}),
            'duration_for_previous':forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter previous Durations in days'}),
            'number_family_close':forms.TextInput(attrs={'class': 'form-control','placeholder':'Number of family Member if Yes'}),
            'relationship':forms.TextInput(attrs={'class': 'form-control','placeholder':'Relationship'}),
            'other_referred':forms.TextInput(attrs={'class': 'form-control','placeholder':'Other referre'}),
            'diagnosis':forms.TextInput(attrs={'class': 'form-control','placeholder':'diagnosis'}),
            'date_enregistrement': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'placeholder': 'Select a date','type': 'date'}),
            'weigth':forms.TextInput(attrs={'class': 'form-control'}),
            'pregnant':forms.Select(attrs={'class':'form-control'}),
            'HIV_status':forms.Select(attrs={'class':'form-control'}),
            'TB_status':forms.Select(attrs={'class':'form-control'}),
            'limitation_mov':forms.Select(attrs={'class':'form-control'}),
            'limitation_daily_act':forms.Select(attrs={'class':'form-control'}),
            'category_lesion': forms.Select(attrs={'class':'form-control'}),
            'no_lesions':forms.TextInput(attrs={'class': 'form-control'}),
            'diameter':forms.TextInput(attrs={'class': 'form-control'}),
            'Clinical_form':forms.TextInput(attrs={'class': 'form-control'}),
            'Location_lesion':forms.TextInput(attrs={'class': 'form-control'}),

           
            

        }
      
        #clinical_forms = forms.MultipleChoiceField(choices=CLINICAL_FORMS, widget=forms.CheckboxSelectMultiple())
       
        
        #clininical_form=forms.MultipleChoiceField(choices=CLINICAL_FORMS,widget=forms.CheckboxSelectMultiple())
        #location_lesion=forms.MultipleChoiceField(choices=LESION_LOCATION,widget=forms.CheckboxSelectMultiple())
        #location_lesion=forms.MultipleChoiceField(choices=LESION_LOCATION,widgets=forms.CheckboxSelectMultiple())
        #couleur=forms.MultipleChoiceField(widget=SelectMultiple(attrs={'class': 'selectpicker'}), choices=FAVORITE_COLORS_CHOICES)
        

       




       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        #Other_detection_mode=forms.CharField(required=False)
        #def clean(self):
           # cleaned_data = super().clean()
        #detection_mode = cleaned_data.get('detection_mode')
        #autres_couleur = cleaned_data.get('Other_detection_mode')
        #if 'autres' in detection_mode and not Other_detection_mode:
            #raise forms.ValidationError("Entrer un mode ")
         #return cleaned_data
    









        #Region =   forms.ChoiceField(choices=Region_CHOICES)  
        #District=  forms.ChoiceField(choices=DISTRICT_CHOICES)
      
