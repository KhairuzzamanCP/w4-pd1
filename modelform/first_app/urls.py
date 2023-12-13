from django.urls import path
from .import views
urlpatterns = [
   path('form/', views.form, name='form'),
   path('model/', views.model_form, name= 'model_form')
]
