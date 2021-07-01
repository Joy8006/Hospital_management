from .models import Hospital, Patient, Report
from .serializers import HospitalSerializer, PatientSerializer, ReportSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class HospitalListCreateAPIView(ListCreateAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.order_by("-id").all()


class HospitalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()


class PatientListCreateAPIView(ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.order_by('-id').all()


class PatientRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class ReportListCreateAPIView(ListCreateAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.order_by('-id').all()


class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
