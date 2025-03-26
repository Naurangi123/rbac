# permissions.py
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Teacher'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Student'
