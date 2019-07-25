from django.urls import path
from . import views

urlpatterns = [
    path('',                   views.index,      name='index'),
    path('Dentist/',           views.index_den,  name='index_den'),
    path('Psychiatrist/',      views.index_psy,  name='index_psy'),
    path('Cardiologist/',      views.index_card, name='index_card'),
    path('Gynaecologist/',     views.index_gyn,  name='index_gyn'),
    path('Hospitalist/',       views.index_hos,  name='index_hos'),
    path('Neurologist/',       views.index_neuro,name='index_neuro'),
    path('Oncologist/',        views.index_onco, name='index_onco'),
    path('Radiologist/',       views.index_rad,  name='index_rad'),
    path('Pulmonologist/',     views.index_pul,  name='index_pul'),
    path('Orthopaedic_Surgeon/',  views.index_orth_surg,  name='index_orth_surg'),
    path('Ophthalmologist/',     views.index_opth,  name='index_opth'),
    
    path('booking/',      views.booking,    name='booking'),
]
