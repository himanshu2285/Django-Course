from django.urls import path
from .views import receipes, delete_receipe, update_receipe

urlpatterns = [
    path('receipes/', receipes, name='receipes'),
    path('delete-receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update-receipe/<int:id>/', update_receipe, name='update_receipe'),

]