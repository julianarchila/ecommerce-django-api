""" Cart permissions. """

from rest_framework.permissions import BasePermission


class IsCartItemOwner(BasePermission):
    """ Is cart item owner.
    Checks if the cart item belongs to the requesting user.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.cart.user