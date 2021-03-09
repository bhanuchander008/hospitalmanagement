from rest_framework import serializers, fields
from .models import Doctor, Patient, Appointment
from django.http import HttpResponse, HttpResponseNotFound

# serializers for doctor model
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("__all__")

    

#serializers for patient model
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'patient_name', 'email',
                  'password', 'mobile', 'adress', 'gender')



#serializers for appointment model
class AppointmentSerializer(serializers.ModelSerializer):
    date = fields.DateField(input_formats=['iso-8601'])

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'time', 'patient_id', 'doctor_id')
    #create the  appointment instance
    def create(self, validated_data):
        obj = Appointment.objects.filter(patient_id=validated_data["patient_id"]
        ,doctor_id=validated_data["doctor_id"],date=validated_data["date"])

        if obj.exists():
            raise serializers.ValidationError(
                "already taken appoinment taken today")
        obj = Appointment.objects.create(
            patient_id=validated_data['patient_id'],
            date=validated_data['date'],
            time=validated_data['time'],
            doctor_id=validated_data['doctor_id'])
        return obj
