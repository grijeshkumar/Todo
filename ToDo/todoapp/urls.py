from django.urls import path , include
from . import views
from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo',TodoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('',include(router.urls))
]
