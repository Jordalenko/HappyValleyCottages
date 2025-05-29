from django.urls import path
from .views import CottageList

urlpatterns = [
    path('', CottageList.as_view(), name='home'),
]