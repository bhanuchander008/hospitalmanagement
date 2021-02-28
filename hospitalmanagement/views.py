from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from .models import Doctor, Patient, Appointment

# view for doctor
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('name')
    serializer_class = DoctorSerializer

# view for Patient
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

#view for appointment
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
