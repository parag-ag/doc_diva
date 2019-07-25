from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Doctor, Dentist, Psychiatrist, Cardiologist, Gynaecologist, Hospitalist, Neurologist, Oncologist, Radiologist, Pulmonologist, Orthopaedic_Surgeon, Ophthalmologist

# Create your views here.

def index(request):
    doc = Doctor.objects.order_by('id')
    return render(request, 'appointment/index.html', {'doc': doc})

def index_den(request):
    doc = Doctor.objects.order_by('id')
    den = Dentist.objects.order_by('init_date')
    den_choice = get_object_or_404(Dentist)
    try:
        selected_choice = den_choice.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Dentist.DoesNotExist):
        return render(request, 'appointment/den_book.html', {'den': den})
        
#    return render(request, 'appointment/index_den.html', {'den': den})
    return render(request, 'appointment/index_den.html', {'doc': doc, 'den': den})

def index_psy(request):
    doc = Doctor.objects.order_by('id')
    psy = Psychiatrist.objects.order_by('init_date')
    return render(request, 'appointment/index_psy.html', {'doc': doc, 'psy': psy})

def index_card(request):
    doc = Doctor.objects.order_by('id')
    card = Cardiologist.objects.order_by('init_date')
    return render(request, 'appointment/index_card.html', {'doc': doc, 'card': card})

def index_gyn(request):
    doc = Doctor.objects.order_by('id')
    gyn = Gynaecologist.objects.order_by('init_date')
    return render(request, 'appointment/index_gyn.html', {'doc': doc, 'gyn': gyn})

def index_hos(request):
    doc = Doctor.objects.order_by('id')
    hos = Hospitalist.objects.order_by('init_date')
    return render(request, 'appointment/index_hos.html', {'doc': doc, 'hos': hos})

def index_neuro(request):
    doc = Doctor.objects.order_by('id')
    neuro = Neurologist.objects.order_by('init_date')
    return render(request, 'appointment/index_neuro.html', {'doc': doc, 'neuro': neuro})

def index_onco(request):
    doc = Doctor.objects.order_by('id')
    onco = Oncologist.objects.order_by('init_date')
    return render(request, 'appointment/index_onco.html', {'doc': doc, 'onco': onco})    

def index_rad(request):
    doc = Doctor.objects.order_by('id')
    rad = Radiologist.objects.order_by('init_date')
    return render(request, 'appointment/index_rad.html', {'doc': doc, 'rad': rad})

def index_pul(request):
    doc = Doctor.objects.order_by('id')
    pul = Pulmonologist.objects.order_by('init_date')
    return render(request, 'appointment/index_pul.html', {'doc': doc, 'pul': pul})

def index_orth_surg(request):
    doc = Doctor.objects.order_by('id')
    orth_surg = Orthopaedic_Surgeon.objects.order_by('init_date')
    return render(request, 'appointment/index_orth_surg.html', {'doc': doc, 'orth_surg': orth_surg})

def index_opth(request):
    doc = Doctor.objects.order_by('id')
    opth = Ophthalmologist.objects.order_by('init_date')
    return render(request, 'appointment/index_opth.html', {'doc': doc, 'opth': opth})



def booking(request):
    doctor = get_object_or_404(Dentist)
    return render(request, 'appointment/booking.html', {'doctor': doctor})
