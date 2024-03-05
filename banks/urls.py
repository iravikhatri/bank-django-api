from django.urls import path
from . import views


urlpatterns = [
    path('', views.BankListAPIView.as_view()),
    path('<int:pk>/', views.BankDetailAPIView.as_view())
]
