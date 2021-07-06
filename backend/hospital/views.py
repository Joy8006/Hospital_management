from rest_framework.permissions import IsAuthenticated
from hospital.permissions import HasPatientPermission
from .models import Hospital, Patient, Report
from .serializers import HospitalSerializer, PatientSerializer, ReportSerializer
from rest_framework.viewsets import ModelViewSet


class HospitalViewSet(ModelViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.order_by("-id").all()


class PatientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasPatientPermission]
    serializer_class = PatientSerializer
    queryset = Patient.objects.order_by('-id').all()


class ReportViewSet(ModelViewSet):
    serializer_class = ReportSerializer
    queryset = Report.objects.order_by('-id').all()