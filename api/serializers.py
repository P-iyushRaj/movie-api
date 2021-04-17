
from rest_framework import serializers
from .models import form_field_model, Patient_model, Patient_address_model
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_field_model
        fields = ['id', 'form_id']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_model
        fields = ['prime_patient_id','prime_first_name','prime_lst_name', 'prime_middle_name', 'prime_suffix_form', 'prime_prefix_form', 'Home_number',
                    'prime_work_number', 'prime_Social_security_num', 'prime_education', 'prime_emergency_phone', 'prime_emergency_name', 'prime_emergency_relation',
                    'prime_sex', 'date_of_birth', 'employee_signature', 'alter_phone', 'alter_name', 'alter_relation']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_address_model
        fields = ['prime_address_id', 'prime_address_street', 'address_street2', 'prime_address_city', 
                    'prime_address_state',]
