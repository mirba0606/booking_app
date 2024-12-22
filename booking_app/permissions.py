from rest_framework import permissions


class CheckCreateHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return True
        return False


class ReviewHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_name:
            return True
        return False
