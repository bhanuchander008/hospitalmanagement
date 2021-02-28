from rest_framework import serializers, fields
from .models import Doctor, Patient, Appointment
from django.http import HttpResponse, HttpResponseNotFound

# serializers for doctor model
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id,''name', 'email', 'password', 'desgination', 'adress')

    def create(self, validated_data):

        # Create the Doctor instance
        obj = Doctor.objects.create(
            name=validated_data['name'], email=validated_data['email'], desgination=validated_data['desgination'])

        return obj
    # update the doctor instance
    def update(self, instance, validated_data):
        # Update the Foo instance
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.desgination = validated_data['desgination']
        instance.password = validated_data['password']
        instance.adress = validated_data['adress']
        instance.save()
        return instance

#serializers for patient model
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ('id', 'patient_name', 'email',
                  'password', 'mobile', 'adress', 'gender')

    def create(self, validated_data):

        # Create the patient instance
        obj = Patient.objects.create(
            patient_name=validated_data['patient_name'], email=validated_data['email'])

        return obj

    def update(self, instance, validated_data):
        # Update the  patient instance
        instance.patient_name = validated_data['patient_name']
        instance.email = validated_data['email']
        instance.gender = validated_data['gender']
        instance.password = validated_data['password']
        instance.adress = validated_data['adress']
        instance.save()
        return instance

#serializers for appointment model
class AppointmentSerializer(serializers.ModelSerializer):
    date = fields.DateField(input_formats=['iso-8601'])

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'time', 'patient_id', 'doctor_id')
    #create the  appointment instance
    def create(self, validated_data):
        obj = Appointment.objects.all()
        for x in obj:
            patient_id = x.patient_id
            ids = patient_id.id
            date = x.date
            patient = validated_data['patient_id']
            id = patient_id.id
            da = validated_data['date']
            if (ids == (id)) and (date == da):
                raise serializers.ValidationError(
                    "already taken appoinment taken today")
        obj = Appointment.objects.create(
            patient_id=validated_data['patient_id'], date=validated_data['date'], time=validated_data['time'], doctor_id=validated_data['doctor_id'])
        return obj

    def update(self, instance, validated_data):
        # Update the appointment instance
        instance.patient_id = validated_data['patient_id']
        instance.doctor_id = validated_data['doctor_id']
        instance.date = validated_data['date']
        instance.time = validated_data['time']
        instance.save()
        return instance
