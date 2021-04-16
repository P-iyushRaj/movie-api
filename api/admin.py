from django.contrib import admin

# Register your models here.
from .models import form_field_model, primerx_field_model

@admin.register(form_field_model)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']

@admin.register(primerx_field_model)
class PdfAdmin(admin.ModelAdmin):
    list_display = ['id', 'prime_first_name']