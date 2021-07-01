from hospital.models import Hospital, Patient, Report
from rest_framework import serializers


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    reports = ReportSerializer(read_only=True, many=True)

    class Meta:
        model = Patient
        fields = '__all__'

