from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class form_field_model(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank =True )
    lst_name = models.CharField(max_length=200, null=True, blank =True )
    middle_name = models.CharField(max_length=200, null=True, blank =True )
    suffix_form = models.CharField(max_length=200, null=True, blank =True )
    prefix_form = models.CharField(max_length=200, null=True, blank =True )
    Home_number = PhoneNumberField( null=True, blank =True )
    work_number = PhoneNumberField( null=True, blank =True )
    Social_security_num = models.IntegerField( null=True, blank =True )

    education = models.CharField(max_length=200, null=True, blank =True ) #checkbox

    address_street = models.CharField(max_length=200, null=True, blank =True )
    address_city = models.CharField(max_length=200, null=True, blank =True )
    address_state = models.CharField(max_length=200, null=True, blank =True )
    address_zip = models.IntegerField( null=True, blank =True )
    emergency_phone = PhoneNumberField( null=True, blank =True )
    emergency_name = models.CharField(max_length=200, null=True, blank =True )
    emergency_relation = models.CharField(max_length=200, null=True, blank =True )

    sex = models.CharField(max_length=200, null=True, blank =True )  #checkbox
    date_of_date = models.DateTimeField(null = True, blank = True)   #"date_of_date": "2021-04-16T14:34:00Z"
    employee_signature = models.FileField(upload_to='upload/', null = True, blank = True)

    objects = models.Manager()


class primerx_field_model(models.Model):
    id = models.BigAutoField(primary_key=True)
    prime_first_name = models.CharField(max_length=200, null=True, blank =True )
    prime_lst_name = models.CharField(max_length=200, null=True, blank =True )
    prime_middle_name = models.CharField(max_length=200, null=True, blank =True )
    prime_suffix_form = models.CharField(max_length=200, null=True, blank =True )
    prime_prefix_form = models.CharField(max_length=200, null=True, blank =True )
    prime_work_number = PhoneNumberField( null=True, blank =True )
    prime_Social_security_num = models.IntegerField( null=True, blank =True )

    prime_education = models.CharField(max_length=200, null=True, blank =True ) #checkbox

    prime_address_street = models.CharField(max_length=200, null=True, blank =True )
    prime_address_city = models.CharField(max_length=200, null=True, blank =True )
    prime_address_state = models.CharField(max_length=200, null=True, blank =True )
    
    prime_emergency_phone = PhoneNumberField( null=True, blank =True )
    prime_emergency_name = models.CharField(max_length=200, null=True, blank =True )
    prime_emergency_relation = models.CharField(max_length=200, null=True, blank =True )

    prime_sex = models.CharField(max_length=200, null=True, blank =True )  #checkbox

    objects = models.Manager()
