from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *
router = routers.DefaultRouter()

# routing for doctor
router.register(r'doctor', views.DoctorViewSet)

#routing for patient
router.register(r'patient', views.PatientViewSet)


# routing for appointment
router.register(r'appointment', views.AppointmentViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
