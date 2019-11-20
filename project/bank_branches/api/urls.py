from django.urls import path
from . import views

urlpatterns = [
    path('banks/', views.BanksApiView.as_view())
]
