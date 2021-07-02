from hospital.models import Hospital, Patient, PatientDataPermission, Report
from django.contrib import admin


class HospitalAdmin(admin.ModelAdmin):
    list_display = ["name", 'address']

class PatientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "address",
        "date_of_birth",
        "weight",
        "height",
        "previous_medical_study",
        "blood_group",
        "blood_pressure",
        "sugar_level",
        "hospital"
    ]
    list_filter = ["hospital"]


class ReportAdmin(admin.ModelAdmin):
    list_display = ["name", "picture", "patient"]


class PatientPermissionAdmin(admin.ModelAdmin):
    list_display = ["patient", "user", "time_start", "time_end", "is_active"]


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(PatientDataPermission, PatientPermissionAdmin)
