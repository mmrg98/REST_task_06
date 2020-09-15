from rest_framework.permissions import BasePermission
from django.utils import timezone
class IsOwner(BasePermission):
    message = "You must be the owner of this book."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False
class ThreeDaysAway(BasePermission):
    message = "too late"
    def has_object_permission(self, request, view, obj):
        return (obj.date - timezone.now().date()).days > 3
