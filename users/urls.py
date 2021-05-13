# Django
from django.urls import path, include

# Django REST Framework.
from rest_framework.routers import DefaultRouter

# Views
from users.views.users import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path("", include(router.urls))
]