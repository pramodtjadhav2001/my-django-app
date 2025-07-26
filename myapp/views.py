from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import HOME
from myadmin.models import ABOUT1,CONTACT1,PIZZA,SALADS,STARTER,CONTACT_INFO,DAY1

# Create your views here.


def home(request):
    data=HOME.objects.get(id=1)
    obj={'data':data}
    
    return render(request,"web/home.html",obj)

def about(request):
    a_data=ABOUT1.objects.get(id=2)
    D_data=DAY1.objects.get(id=1)
    obj={'a_data':a_data,'D_data':D_data}
    return render(request,"web/about.html",obj)


def menu(request):
    p_data=PIZZA.objects.all()
    s_data=SALADS.objects.all()
    st_data=STARTER.objects.all()
    obj={'p_data':p_data,'s_data':s_data,'st_data':st_data}
    return render(request,"web/menu.html",obj)



def contact(request):
    ci_data=CONTACT_INFO.objects.get(id=1)
    obj={'ci_data':ci_data}
    return render(request,"web/contact.html",obj)


