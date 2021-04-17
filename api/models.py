from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Patient_model(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    prime_patient_id = models.IntegerField( null=True, blank =True )
    prime_first_name = models.CharField(max_length=200, null=True, blank =True )
    prime_lst_name = models.CharField(max_length=200, null=True, blank =True )
    prime_middle_name = models.CharField(max_length=200, null=True, blank =True )
    prime_suffix_form = models.CharField(max_length=200, null=True, blank =True )
    prime_prefix_form = models.CharField(max_length=200, null=True, blank =True )
    Home_number = PhoneNumberField( null=True, blank =True )
    prime_work_number = PhoneNumberField( null=True, blank =True )
    prime_Social_security_num = models.IntegerField( null=True, blank =True )
    prime_education = models.CharField(max_length=200, null=True, blank =True ) #checkbox

    prime_emergency_phone = PhoneNumberField( null=True, blank =True )
    prime_emergency_name = models.CharField(max_length=200, null=True, blank =True )
    prime_emergency_relation = models.CharField(max_length=200, null=True, blank =True )
    prime_sex = models.CharField(max_length=200, null=True, blank =True )  #checkbox
    date_of_birth = models.DateTimeField(null = True, blank = True)   #"date_of_date": "2021-04-16T14:34:00Z"
    employee_signature = models.FileField(upload_to='upload/', null = True, blank = True)

    #morefields
    alter_phone = PhoneNumberField( null=True, blank =True )
    alter_name = models.CharField(max_length=200, null=True, blank =True )
    alter_relation = models.CharField(max_length=200, null=True, blank =True )

    objects = models.Manager()

#think as prescriber
class Patient_address_model(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    prime_address_id = models.IntegerField( null=True, blank =True )
    prime_address_street = models.CharField(max_length=200, null=True, blank =True )
    address_street2 = models.CharField(max_length=200, null=True, blank =True )
    prime_address_city = models.CharField(max_length=200, null=True, blank =True )
    prime_address_state = models.CharField(max_length=200, null=True, blank =True )
    address_zip = models.IntegerField( null=True, blank =True )

    objects = models.Manager()

# Create your models here.
class form_field_model(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.IntegerField( null=True, blank =True )
    #foreign key to patient and address
    Patient = models.ForeignKey(
        'Patient_model', on_delete=models.SET_NULL, blank=True, null=True
        )
    address = models.ForeignKey(
        'Patient_address_model', on_delete=models.SET_NULL, blank=True, null=True
        )

    objects = models.Manager()


