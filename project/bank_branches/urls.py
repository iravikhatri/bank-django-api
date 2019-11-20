from django.urls import path, include

urlpatterns = [
    path('api/', include('bank_branches.api.urls')),
]
