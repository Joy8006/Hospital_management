from django.db import models
from django.conf import settings


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Hospital(TrackingModel):

    name = models.CharField(max_length=500, blank=False, null=False)
    address = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Patient(TrackingModel):
    BLOOD_GROUP = [
        ("A+", "A+"),
        ("B+", "B+"),
        ("O+", "O+"),
        ("AB+", "AB+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("AB-", "AB-")
    ]
    name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=False, null=True)
    weight = models.FloatField(default=0, null=True)
    height = models.FloatField(default=0, null=True)
    previous_medical_study = models.TextField(blank=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP, blank=True, null=True)
    blood_pressure = models.CharField(max_length=10, default="0/0", null=True)
    sugar_level = models.FloatField(default=0, null=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=False, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=False, null=True)


    def __str__(self):
        return self.name


class Report(TrackingModel):

    name = models.CharField(max_length=100, blank=False, null=True)
    picture = models.ImageField(blank=False, null=True, upload_to="images/reports/%Y/%m")
    patient = models.ForeignKey(Patient, related_name="reports", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name