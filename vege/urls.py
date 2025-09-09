from django.urls import path
from .views import receipes

urlpatterns = [
    path('receipes/', receipes, name='receipes'),
]