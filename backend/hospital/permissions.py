from rest_framework.permissions import BasePermission
from django.utils import timezone
from hospital.models import PatientDataPermission


class HasPatientPermission(BasePermission):
    """
    Allows access only to admin users or own account
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user:
            return False

        permissions = PatientDataPermission.objects.filter(user=user, patient=obj, is_active=True)
        print(permissions)
        if permissions.exists():
            current_time = timezone.now()
            permission = permissions.first()
            
            if permission.time_end < current_time:
                permission.time_end = current_time
                permission.is_active = False
                permission.save()
                return False
            else:
                return True
        return False