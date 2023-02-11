from django.db import models

# Create your models here.
class Patient(models.Model):
    datetime_signin = models.DateTimeField(auto_now_add=True)
    # Personal info
    patient_id = models.CharField(max_length=100, unique=True)
    patient_name = models.CharField(max_length=100)
    patient_fathers_ln = models.CharField(max_length=100)
    patient_monthers_ln = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthday = models.DateTimeField()
    # year_birth = models.IntegerField()
    # month_birth = models.IntegerField()
    # day_birth = models.IntegerField()
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

    def __str__(self):
        return self.patient_name