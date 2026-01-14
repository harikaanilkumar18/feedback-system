from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_list, name='form_list'),
    path('<int:form_id>/', views.fill_form, name='fill_form'),
    path('<int:form_id>/submit/', views.submit_form, name='submit_form'),
]
