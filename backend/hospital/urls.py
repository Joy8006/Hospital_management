from .views import (
    HospitalListCreateAPIView,
    HospitalRetrieveUpdateDestroyAPIView,
    PatientListCreateAPIView,
    PatientRetrieveUpdateDestroyAPIView,
    ReportListCreateAPIView,
    ReportRetrieveUpdateDestroyAPIView
)
from django.urls import path


urlpatterns = [
    path("hospitals/", HospitalListCreateAPIView.as_view()),
    path("hospitals/<str:pk>/", HospitalRetrieveUpdateDestroyAPIView.as_view()),
    path("patients/", PatientListCreateAPIView.as_view()),
    path("patients/<str:pk>/", PatientRetrieveUpdateDestroyAPIView.as_view()),
    path("reports/", ReportListCreateAPIView.as_view()),
    path("reports/<str:pk>/", ReportRetrieveUpdateDestroyAPIView.as_view()),
]
