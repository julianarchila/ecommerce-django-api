

# Django
from django.urls import path, include

# Django REST Framework.
from rest_framework.routers import DefaultRouter

# Views
from products.views.products import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path("", include(router.urls))
]