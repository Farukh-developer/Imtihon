

from django.shortcuts import render, get_object_or_404, redirect
from .models import Tour, Service, Parvoz, Yunalish
from .forms import Serviceform
# from .forms import 
 

def home(request):
    services=Service.objects.all()
    tour=Tour.objects.all()
    parvoz=Parvoz.objects.all()
    return render(request, 'home.html', context={"services":services, "tour":tour, "parvoz":parvoz})

    
  
def read(request, id):
    service=Service.objects.get(id=id)
    return render(request, 'read_home.html', context={"service":service})

def create(request):
    form=Serviceform()
    if request.method=='POST':
        form=Serviceform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'create.html', context={"form":form})   


##########

def update(request, id):
    service=get_object_or_404(Service, id=id)
    form=Serviceform(instance=service)
    if request.method=='POST':
        form=Serviceform(request.POST,request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'create.html', context={"form":form})    

def delete(request, id):
    service=get_object_or_404(Service, id=id)
    service.delete()
    return redirect('/home')    


def tour(request, id):
    tour=get_object_or_404(Tour, id=id)
    services=tour.tour.all()
    tour=Tour.objects.all()
    return render(request, 'home.html', context={"services":services, "tour":tour})


#######


def about(request):
    service=Service.objects.all()
    tour=Tour.objects.all()
    return render(request, 'about.html', context={"service":service,"tour":tour} )

def view(request, service_id):
    service =Service.objects.get(id=service_id)
    tour=Tour.objects.all()
    return render(request, 'view.html', context={"service": service, "tour":tour})

def contact(request):
    service=Service.objects.all()
    tour=Tour.objects.all()
    return render(request, 'contact.html', context={"service":service, "tour":tour})



########


def yunalish(request):
    yunalish=Yunalish.objects.all()
    parvoz=Parvoz.objects.all()
    return render(request, 'yunalish.html', context={"yunalish":yunalish, "parvoz":parvoz})

def parvoz(request, id):
    parvoz=get_object_or_404(Parvoz, id=id)
    yunalish=parvoz.air.all()
    parvoz=Parvoz.objects.all()
    return render(request, 'yunalish.html', context={"parvoz":parvoz, "yunalish":yunalish})

def overall(request, id):
    yunalish =get_object_or_404(Yunalish, id=id)
    parvoz=Parvoz.objects.all()
    tour=Tour.objects.all()
    return render(request, 'overall.html', context={"yunalish":yunalish, "parvoz":parvoz,"tour":tour})
    



