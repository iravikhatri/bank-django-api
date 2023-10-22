from django.urls import path
from . import views


urlpatterns = [
    path('', views.BankAPIView.as_view())
]
