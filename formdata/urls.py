from django.urls import path
from .views import add_form_data,list_form_data

urlpatterns = [
    path('form_data/add', add_form_data),
    path('form_data/list', list_form_data)
]