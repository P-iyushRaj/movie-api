from django.contrib import admin

# Register your models here.
from .models import form_field_model, Patient_model, Patient_address_model

@admin.register(form_field_model)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id','form_id']

@admin.register(Patient_model)
class patientAdmin(admin.ModelAdmin):
    list_display = ['patient_id']

@admin.register(Patient_address_model)
class addressAdmin(admin.ModelAdmin):
    list_display = ['address_id']