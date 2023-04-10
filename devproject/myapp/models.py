from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime, date


# Create your models here.
class Employee(models.Model):  
    #Modele de donnee concernant la partie SKIN NTDS clinical and treatment form
    
    Health_facility = models.CharField(max_length=200)  
    worker_health_name = models.CharField(max_length=150)  
    patient_name  = models.CharField(max_length=150)
    patient_ID = models.CharField(max_length=50)
    Date_of_birth = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    Country = models.CharField(max_length=100)
    Region_CHOICES = [('Adamaoua', 'Adamaoua'),('Centre','Centre'),('Est','Est'),('Extrême Nord','Extrême Nord'),('Littoral','Litoral'),
        ('Nord','Nord'),('Nord Ouest','Nord ouest'),('Ouest','Ouest'),('Sud','Sud'),('Sud Ouest','Sud Ouest')]
    Region =models.CharField(max_length=20,choices= Region_CHOICES,null=True)
    DISTRICT_CHOICES = [('Bankim','Bankim'),('Banyo','Banyo'),('Dang','Dang'),('Tibati','Tibati'),('Ngaoundere Rural','Ngaoundere Rural')]
    District =models.CharField(max_length=40, choices= DISTRICT_CHOICES, null = True)
    SEXE_CHOICES = [('masculin', 'Male'), ('feminin', 'Female')]
    sexe = models.CharField(max_length=8, choices=SEXE_CHOICES, null=True)
    Village = models.CharField(max_length=150)
    Phone_number = models.CharField(max_length=12, blank=True)
    Occupation = models.CharField(max_length=150)
    Landmark = models.CharField(max_length=150)
    Contact_person = models.CharField(max_length=250)
    Contact_person_phone = models.CharField( max_length=12, blank=True)

    # Modeles de donnees concernant la section History of admission

    DETECTION_CHOICES=[
                            ('Active screening','Active screening'),('School survey', 'School survey '),
                           ('Referred','Referred'),('Passive','Passive'),('Other','Other') 
                           ]
    

    


    CLASSIFICATION=[  ('New','New'), ('Recurrent','Recurent')]

    TRADITIONAL= [('Yes','Yes'), ('No','No')]

    PREGNANT_LIST=[('Yes','Yes'), ('No','No'),('Unknown','Unknown')]

    INITIAL_CLINICAL=[('Positive','Positive'), ('Negative','Negative'),('Unknown','Unknown')]

    CLINICAL_FORMS=[('Nodule','Nodule'), ('Papule','Papule'),('Ulcere','Ulcere'),('Oedema','Oedema'),('Osteomyetlitis','Osteomyelitis')]    

    REFERRED=[('self-referral','self-referral'),('Health worker','Health worker'), ('Village','Village'),('Traditional healer','Traditional healer'),
              ('Family member','Family member'), ('Former patient','Former patient'), ('School Teacher', 'School Teacher'),('Other','Other')]
    
    LESION_LOCATION=[('Abdomen','Abdomen'),('Back','Back'),('Breast','Breast'),('Buttocks and perineum','Buttocks and perineum'),('Eye','Eye'),('Genitalia','Genitalia'),
                     ('Head and Neck','Head and Neck'), ('Inguinal/Groin','Inguinal/Groin'), ('Lower Limb','Lower Limb'),
                     ('Thorax','Thorax'),('Upper Limb','Upper Limb')]
    
    CATEGORY=[('Category I','Category I'),('Category II','Category II'),('Category III','Category III')]
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    
   
    detection_mode=models.CharField(max_length=100, choices= DETECTION_CHOICES, null=False)
    classification=models.CharField(max_length=100, choices=CLASSIFICATION)
    duration_illnes=models.PositiveIntegerField(blank=False)
    use_traditional=models.CharField(max_length=100, choices=TRADITIONAL)
    any_treat=models.CharField(max_length=50,choices=TRADITIONAL)
    treat_prev=models.CharField(max_length=50, choices=TRADITIONAL)

    Referred_by=models.CharField(max_length=30,choices=REFERRED,null=True)

    Family_member=models.CharField(max_length=50, choices=TRADITIONAL)
    other_mode_detection=models.CharField(max_length=200, null=True, blank= True)
    specify_any_treatment=models.CharField(max_length=200, null=True, blank= True)
    duration_any=models.CharField(max_length=200, null=True, blank= True)
    specify_for_previous=models.CharField(max_length=200, null=True, blank= True)
    duration_for_previous=models.CharField(max_length=200, null=True, blank= True)
    number_family_close=models.CharField(max_length=200, null=True, blank= True)
    
    TB_status=models.CharField(max_length=30, choices=INITIAL_CLINICAL)
    limitation_mov=models.CharField(max_length=30, choices=TRADITIONAL)
    limitation_daily_act=models.CharField(max_length=30,choices= TRADITIONAL)
    date_enregistrement=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    relationship=models.CharField(max_length=150, null=True, blank=True)
    weigth=models.CharField(max_length=150)
    pregnant=models.CharField(max_length=30, choices=PREGNANT_LIST)
    HIV_status=models.CharField(max_length=30, choices=INITIAL_CLINICAL)
    diagnosis=models.CharField(max_length=150, null=True, blank=True)
    other_referred=models.CharField(max_length=150, null=True, blank=True)
   
    #clininical_form=MultiSelectField(max_length=50, max_choices=6, choices=CLINICAL_FORMS, default='none')
    #location_lesion=MultiSelectField(max_length=50, max_choices=9, choices=LESION_LOCATION, default='none')
    category_lesion=models.CharField(max_length=50,choices=CATEGORY)
    no_lesions=models.CharField(max_length=4,null=True, blank=True)
    diameter=models.CharField(max_length=10, null=True, blank=True)
    #couleur=models.CharField(max_length=250, choices=FAVORITE_COLORS_CHOICES, default='blue')
    Clinical_form=models.CharField(max_length=250, null=True, blank=True)
    Location_lesion=models.CharField(max_length=250, null=True, blank=True)
    


    
