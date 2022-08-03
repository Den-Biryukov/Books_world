from rest_framework.permissions import BasePermission, SAFE_METHODS

# Permission for delete
class IsOwnerOrStaffOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and (obj.owner == request.user
                                               or request.user.is_staff)
        )

# Permission for update
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.owner == request.user
        )

# for likes and rating
class UserIsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and obj.user == request.user
        )


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsAuthOrStaffOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated or request.user.is_staff
        )


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)
