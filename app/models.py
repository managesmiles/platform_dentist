# from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
    datetime_signin = models.DateTimeField(auto_now_add=True)

    # Personal info
    patient_id = models.CharField(max_length=15, primary_key=True)
    patient_name = models.CharField(max_length=100)
    patient_fathers_ln = models.CharField(max_length=100)
    patient_monthers_ln = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    # birthday = models.DateTimeField()
    year_birth = models.PositiveSmallIntegerField()
    month_birth = models.PositiveSmallIntegerField()
    day_birth = models.PositiveSmallIntegerField()

    # Contact
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    
    # Adress
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    
    # Education
    profession = models.CharField(max_length=50, default=None, null=True)
    education_level = models.CharField(max_length=50, default=None, null=True)

    # def __str__(self):
    #     return self.patient_name


class Dentist(models.Model):
    datetime_signin = models.DateTimeField(auto_now_add=True)
    dentist_id = models.CharField(max_length=15, primary_key=True)

    # Personal info
    dentist_name = models.CharField(max_length=100)
    dentist_fathers_ln = models.CharField(max_length=100)
    dentist_monthers_ln = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    # birthday = models.DateTimeField()
    year_birth = models.PositiveSmallIntegerField()
    month_birth = models.PositiveSmallIntegerField()
    day_birth = models.PositiveSmallIntegerField()

    # year_birth = models.IntegerField()
    # month_birth = models.IntegerField()
    # day_birth = models.IntegerField()

    # Contact
    phone_country_lada = models.CharField(max_length=4)
    phone_number = models.IntegerField()
    email = models.EmailField()

    # Adress
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    
    # Education
    university_name = models.CharField(max_length=50)
    postgrade_name = models.CharField(max_length=50)
    postgrade_u_name = models.CharField(max_length=50)
    
    # Laboral experience
    curr_company_name = models.CharField(max_length=50)
    start_work_year = models.IntegerField()
    start_work_month = models.IntegerField()

    # Message please select your 2 last jobs more rrepresentative
    company_worked_2 = models.CharField(max_length=50)
    start_work_year_2 = models.IntegerField( default=None, null=True)
    start_work_month_2 = models.IntegerField( default=None, null=True)
    
    company_worked_3 = models.CharField(max_length=50)
    start_work_year_3 = models.IntegerField( default=None, null=True)
    start_work_month_3 = models.IntegerField( default=None, null=True)

    # def __str__(self):
    #     return self.dentist_name


class TreatmentTape(models.Model):
    datetime_apppointment = models.DateTimeField(auto_now_add=True)
    # Id :3(COUNTRY) :3(STATE), :3(LAST_NAME), :2(BIRTH) 3(Number_of_appointment)001,002...999
    treatment_id = models.CharField(max_length=15, primary_key=True)

    # Foreign Keys
    dentist_id = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # Treatment
    treatment_name = models.CharField(max_length=100)
    treatment_status = models.CharField(max_length=100) # (started, in progress, finished)}
    treatment_priority = models.CharField(max_length=6) # Low, Medium, High
    treatment_time_hours = models.DecimalField(max_digits=2, decimal_places=2)
    amt_revenue = models.DecimalField(max_digits=8, decimal_places=2)

    # amt_expenses = models.DecimalField(max_digits=8, decimal_places=2)
    material_used_01 = models.CharField(max_length=20, default=None, null=True)
    material_used_02 = models.CharField(max_length=20, default=None, null=True)
    material_used_03 = models.CharField(max_length=20, default=None, null=True)
    material_used_04 = models.CharField(max_length=20, default=None, null=True)
    material_used_05 = models.CharField(max_length=20, default=None, null=True)
    comments = models.TextField(max_length=200, default=None, null=True)

    # next appointment
    nu_follow_appointments = models.PositiveSmallIntegerField()
    priority_next_appointment = models.CharField(max_length=100)
    datetime_next_appointment = models.DateTimeField()

    # Zone, se identifica con dentist_id or patient_id

    # def __str__(self):
    #     return self.treatment_status



# class Material(models.Model):
#     date_bought = models.DateField()
#     material_id = models.CharField(max_length=20, unique=True)

#     dentist_id = models.ForeignKey(Dentist, on_delete=models.CASCADE)#, related_name='materials')

#     material_name = models.CharField(max_length=100, )
#     material_amount = models.PositiveIntegerField()
#     material_price = models.DecimalField(max_digits=8, decimal_places=2 )
#     material_supplier_name = models.CharField(max_length=100)
#     equipment_supplier_country = models.CharField(max_length=100)
#     equipment_supplier_state = models.CharField(max_length=100)
#     months_until_next_supply = models.PositiveIntegerField()
#     # date_expected_supply = models.DateField(null=True, blank=True)

# class Equipment(models.Model):
#     dentist_id = models.ForeignKey(Dentist, on_delete=models.CASCADE)#, related_name='materials')
#     equipment_id = models.CharField(max_length=20, unique=True)

#     equipment_name = models.CharField(max_length=100, )
#     equipment_age = models.PositiveIntegerField()
#     equipment_supplier_name = models.CharField(max_length=100)
#     equipment_supplier_country = models.CharField(max_length=100)
#     equipment_supplier_state = models.CharField(max_length=100)

#     equipment_cost = models.DecimalField(max_digits=8, decimal_places=1)
#     years_remaning_useful_life = models.PositiveIntegerField() # to notify when to renew
#     # date_expected_supply = models.DateField(null=True, blank=True)
