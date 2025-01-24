from django.urls import path
from . import views

urlpatterns = [
    path('', views.certificate_list, name='certificate_list'),
    path('add/', views.add_certificate, name='add_certificate'),
    path('expiration_counts/', views.certificate_expiration_counts, name='certificate_expiration_counts'),
]
