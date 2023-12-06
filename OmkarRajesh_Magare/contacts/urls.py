from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('list/', views.list_contacts, name='list_contacts'),
    path('create/', views.create_contact, name='create_contact'),
    path('update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),



]
