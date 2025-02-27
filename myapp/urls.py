from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('print_message/', views.print_message, name='print-message'),
]
