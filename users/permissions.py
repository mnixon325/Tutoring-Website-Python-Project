from rest_framework import permissions

class IsItselfOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request
        #so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions are only allowed to the owner of the post.
        return obj.username == request.user.username


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #Read permissions are allowed to any request
        #so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        #Write permissions are only allowed to the owner of the post.
        return obj.owner == request.user

class IsTutorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # obj1 = request.user.username.objects.first()
        # field_object = request.user.username._meta.get_field('is_tutor')
        # field_value = field_object.value_from_object(obj1)
        current_user = request.user
        isTutor = current_user.is_tutor
        #Read permissions are allowed to any request
        #so we'll always allow GET, HEAD or OPTIONS requests.
        #if request.method in permissions.SAFE_METHODS:
        if request.method == 'GET' or request.method == 'HEAD' or request.method == 'OPTIONS':
            return True
        else:
            if isTutor == 'true':
            #Write permissions are only allowed to the owner of the post.
                #return obj.owner == request.user
                return request.user.username