from django.urls import path
from .views import (
    add_form_data,
    list_form_data,
    full_update_form_data,
    partial_update_form_data,
    delete_form_data
)

urlpatterns = [
    path('form_data/add', add_form_data),                      # POST
    path('form_data/list', list_form_data),                    # GET
    path('form_data/edit/<int:pk>', full_update_form_data),    # POST (simulate PUT)
    path('form_data/update/<int:pk>', partial_update_form_data),  # POST (simulate PATCH)
    path('form_data/delete/<int:pk>', delete_form_data),       # GET (simulate DELETE)
]
