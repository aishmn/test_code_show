from rest_framework.permissions import BasePermission

class WriteOnly():
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        
        return False