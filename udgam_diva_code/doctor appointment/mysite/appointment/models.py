from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    d_type = models.CharField(max_length = 20)
    def __str__(self):
        return self.d_type


class Dentist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = 10
    works_upto = 19
    init_date = models.IntegerField(default = 1)
    curr_status = models.IntegerField(default = 0)
    max_booking = models.IntegerField(default = 60)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True


class Psychiatrist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField(default = 0)
    works_upto = models.IntegerField(default = 0)
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Cardiologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Gynaecologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Hospitalist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True
    
class Neurologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Oncologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Radiologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Pulmonologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True
    
class Orthopaedic_Surgeon(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True

class Ophthalmologist(models.Model):
    name = models.CharField(max_length = 25)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

    def availability(self):
        now = timezone.now()
        return True
