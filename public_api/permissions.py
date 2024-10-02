from rest_framework.permissions import BasePermission


# Thanks to this StackOverflow post for the permissions handling here.
# https://stackoverflow.com/a/34162842
class UserPermission(BasePermission):

    # Generally for permissions, only allow `list` if we're staff. Allow others based on object permissions.
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    #                                                         
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_staff
        else:
            return False