
from rest_framework import serializers
from .models import form_field_model, primerx_field_model
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_field_model
        fields = ['id','first_name','lst_name', 'middle_name', 'suffix_form', 'prefix_form', 'Home_number',
                    'work_number', 'Social_security_num', 'education', 'address_street', 'address_city', 
                    'address_state', 'address_zip', 'emergency_phone', 'emergency_name', 'emergency_relation',
                    'sex', 'date_of_date', 'employee_signature']

class PrimerxSerializer(serializers.ModelSerializer):
    class Meta:
        model = primerx_field_model
        fields = ['id','prime_first_name','prime_lst_name', 'prime_middle_name', 'prime_suffix_form', 'prime_prefix_form',
                    'prime_work_number', 'prime_Social_security_num', 'prime_education', 'prime_address_street', 'prime_address_city', 
                    'prime_address_state', 'prime_emergency_phone', 'prime_emergency_name', 'prime_emergency_relation',
                    'prime_sex' ]