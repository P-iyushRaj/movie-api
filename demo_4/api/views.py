from django.shortcuts import render

from .models import form_field_model, primerx_field_model
from .serializers import FormSerializer, PrimerxSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView

# Create your views here.
class formListCreate(ListCreateAPIView):
    queryset = form_field_model.objects.all()
    serializer_class = FormSerializer

class primerxList(ListAPIView):
    queryset = primerx_field_model.objects.all()
    serializer_class = PrimerxSerializer