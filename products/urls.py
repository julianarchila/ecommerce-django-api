# Django
from django.urls import path, include

# Django REST Framework.
from rest_framework.routers import DefaultRouter

# Views
from products.views.products import ProductViewSet
from products.views.categories import CategoryViewSet 

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path("", include(router.urls))
]