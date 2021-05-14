""" Orders urls. """

# Django
from django.urls import path, include

# Django REST Framework.
from rest_framework.routers import DefaultRouter

# Views
from orders.views.orders import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')


urlpatterns = [
    path("", include(router.urls))
]