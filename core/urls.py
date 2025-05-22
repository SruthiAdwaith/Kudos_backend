from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KudosViewSet, UserViewSet

router = DefaultRouter()
router.register('kudos', KudosViewSet, basename='kudos')
router.register('user', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
