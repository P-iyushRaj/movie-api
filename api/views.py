from django.shortcuts import render

from .models import form_field_model, Patient_model, Patient_address_model
from .serializers import FormSerializer, PatientSerializer, AddressSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import requests
import pandas as pd

class formListCreate(APIView):
    def get(self, request, pk = None, format=None):
        prime_res = requests.get('https://demo-primerx.herokuapp.com/primerxgetapi/')
        prime_response = prime_res.json()
        primerx_fields = list(prime_response[0].keys())[3:]
        
        if not Patient_model.objects.filter(prime_patient_id=prime_response[0]['prime_patient_id']).exists():
            serializer_pt = PatientSerializer(data = prime_response[0])
            serializer_pt.is_valid()
            serializer_pt.save()
        
        if not Patient_address_model.objects.filter(prime_address_id=prime_response[0]['prime_address_id']).exists():
            serializer_add = AddressSerializer(data = prime_response[0])
            serializer_add.is_valid()
            serializer_add.save()        

        df = pd.read_excel (r'./check_form.xlsx', engine='openpyxl')
        required_field = df.loc[df['form_id_01'] == 'yes']
        required_field_name = required_field['field_name'].values.tolist()

        missing_fields = set(required_field_name).difference(primerx_fields)

        return Response({'msg':'missing_patient_fields, patient, address', 'missing_patient_data':missing_fields, 'primerx_data': prime_response})

    #partial update
    def patch(self,request,pk=None,format=None):
        
        id = pk
        Patient_m = Patient_model.objects.get(pk = id)
        serializer = PatientSerializer(Patient_m,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

