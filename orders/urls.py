""" Orders urls. """

# Django
from django.urls import path, include

# Django REST Framework.
from rest_framework.routers import DefaultRouter

# Views
from orders.views.orders import OrderViewSet
from orders.views.cart import CartViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename='order')
router.register(r'cart', CartViewSet, basename='cart')



urlpatterns = [
    path("", include(router.urls))
]