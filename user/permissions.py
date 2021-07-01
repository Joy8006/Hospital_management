from rest_framework.permissions import BasePermission

class IsAdminUserOrOwnAccount(BasePermission):
    """
    Allows access only to admin users or own account
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        
        if obj == request.user:
            return True
        return False