from django.contrib import admin
from .models import Doctor, Dentist, Psychiatrist, Cardiologist, Gynaecologist, Hospitalist, Neurologist, Oncologist, Radiologist, Pulmonologist, Orthopaedic_Surgeon, Ophthalmologist

# Create your views here.
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Dentist)
admin.site.register(Psychiatrist)
admin.site.register(Cardiologist)
admin.site.register(Gynaecologist)
admin.site.register(Hospitalist)
admin.site.register(Neurologist)
admin.site.register(Oncologist)
admin.site.register(Radiologist)
admin.site.register(Pulmonologist)
admin.site.register(Orthopaedic_Surgeon)
admin.site.register(Ophthalmologist)
