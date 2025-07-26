from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from myapp.models import HOME
from myadmin.models import ABOUT1, CONTACT, PIZZA, SALADS, STARTER, CONTACT_INFO, REGISTRATION, DAY1

# Create your views here.

# -------------------------------(admin contact)-------------------------

def admin(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    return render(request, "admin/admin.html")


# --------------------(home page infomation)-----------------------------

def admin_home(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    data = HOME.objects.all()
    obj = {'data': data}
    return render(request, "admin/admin_home.html", obj)

def save_home(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    home = HOME.objects.get(id=1)
    home.heading = request.POST['heading']
    home.image = request.FILES['img']
    home.save()
    
    print(request.POST)
    return redirect("/admin/admin_home/") 


# -------------(contact infomation page)-------------------------


def c_info(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    ci_data = CONTACT_INFO.objects.all()
    obj = {'ci_data': ci_data}
    return render(request, "admin/c_info.html", obj)


def save_admin_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    c = CONTACT_INFO.objects.get(id=1)
    c.image = request.FILES['img']
    c.heading = request.POST['heading']
    c.caption1 = request.POST['caption1']
    c.caption2 = request.POST['caption2']
    c.caption3 = request.POST['caption3']
    c.save()
    return redirect("/admin/c_info/")


# -------------------------(web contact)----------------------------

def admin_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    ac_data = CONTACT.objects.all()
    obj = {'ac_data': ac_data}
    return render(request, "admin/admin_contact.html", obj)

def save_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    CONTACT.objects.create(
        name=request.POST['Name'],
        people=request.POST['People'],
        date=request.POST['date'],
        message=request.POST['Message'],
    )
    return redirect("/admin/admin_contact/")

def delete_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    id = request.GET['id']
    CONTACT.objects.filter(id=id).delete()
    return redirect("/admin/admin_contact/")

def edit_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    con = CONTACT.objects.get(id=request.GET['id'])
    obj = {'con': con}
    return render(request, "admin/edit_contact.html", obj)

def update_contact(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    cont = CONTACT.objects.get(id=request.POST['id'])
    cont.name = request.POST['edit_name']
    cont.people = request.POST['edit_people']
    cont.date = request.POST['edit_date']
    cont.message = request.POST['edit_message']
    cont.save()
    return redirect("/admin/admin_contact/")


# ----------------------(about information page 1st)-----------------------

def about_info(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    a_data = ABOUT1.objects.all()
    obj = {'a_data': a_data}
    return render(request, "admin/about_info.html", obj)

def save_about_info(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    about1 = ABOUT1.objects.get(id=2)
    about1.heading = request.POST['heading']
    about1.caption1 = request.POST['caption1']
    about1.caption2 = request.POST['caption2']
    about1.caption3 = request.POST['caption3']
    about1.image = request.FILES['image']
    about1.save()
    
    return redirect("/admin/about_info/")


#  ------------------(about infrmation days page 2nd)---------------------
def day(request):    
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    D_data = DAY1.objects.all()
    obj = {'D_data': D_data}
    return render(request, "admin/day.html", obj)

def save_day(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    Day = DAY1.objects.get(id=1)
    Day.sunday1 = request.POST['Sunday1']
    Day.sunday2 = request.POST['Sunday2']
    Day.monday1 = request.POST['Monday1']
    Day.monday2 = request.POST['Monday2']
    Day.tuesday1 = request.POST['Tuesday1']
    Day.tuesday2 = request.POST['Tuesday2']
    Day.wednesday1 = request.POST['Wednesday1']
    Day.wednesday2 = request.POST['Wednesday2']
    Day.thurday1 = request.POST['Thurday1']
    Day.thurday2 = request.POST['Thurday2']
    Day.friday1 = request.POST['Friday1']
    Day.friday2 = request.POST['Friday2']
    Day.saturday1 = request.POST['Saturday1']
    Day.saturday2 = request.POST['Saturday2']
    Day.save()
    return redirect("/admin/day/")


# -----------------(menu pizza page)-------------------------------------

def pizza(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    p_data = PIZZA.objects.all()
    obj = {'p_data': p_data}
    return render(request, "admin/pizza.html", obj)

def save_pizza(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    PIZZA.objects.create(
        heading=request.POST['heading'],
        caption=request.POST['discription'],
        range=request.POST['range'],
    )
    return redirect("/admin/pizza/")

def delete_pizza(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    id = request.GET['id']
    PIZZA.objects.filter(id=id).delete()
    return redirect("/admin/pizza/")

def pizza_edit(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    ep_data = PIZZA.objects.get(id=request.GET['id'])
    obj = {'ep_data': ep_data}
    return render(request, "admin/pizza_edit.html", obj)

def update_pizza(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    piz = PIZZA.objects.get(id=request.POST['id'])
    piz.heading = request.POST['edit_heading']
    piz.caption = request.POST['edit_discription']
    piz.range = request.POST['edit_range']
    piz.save()
    return redirect("/admin/pizza/")


# -----------------(menu salads page)-------------------------------------

def salads(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    s_data = SALADS.objects.all()
    obj = {'s_data': s_data}
    return render(request, "admin/salads.html", obj)

def save_salads(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    SALADS.objects.create(
        heading=request.POST['heading'],
        caption=request.POST['discription'],
        range=request.POST['range'],
    )
    return redirect("/admin/salads/")

def delete_salads(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    id = request.GET['id']
    SALADS.objects.filter(id=id).delete()
    return redirect("/admin/salads/")

def salads_edit(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    info = SALADS.objects.get(id=request.GET['id'])
    obj = {'info': info}
    return render(request, "admin/salads_edit.html", obj)

def update_salads(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    sa = SALADS.objects.get(id=request.POST['id'])
    sa.heading = request.POST['edit_heading']
    sa.caption = request.POST['edit_discription']
    sa.range = request.POST['edit_range']
    sa.save()
    return redirect("/admin/salads/")


# -----------------(menu stater page)-------------------------------------

def starter(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    st_data = STARTER.objects.all()
    obj = {'st_data': st_data}
    return render(request, "admin/starter.html", obj)

def save_starter(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    STARTER.objects.create(
        heading=request.POST['heading'],
        caption=request.POST['discription'],
        range=request.POST['range'],
    )
    return redirect("/admin/starter/")



def delete_stater(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    id=request.GET['id']
    STARTER.objects.filter(id=id).delete()
    return redirect("/starter")

def edit_starter(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    es_data=STARTER.objects.get(id=request.GET['id'])
    obj={'es_data':es_data}
    return render(request,"admin/edit_starter.html",obj)

def update_starter(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    start=STARTER.objects.get(id=request.POST['id'])
    start.heading=request.POST['edit_heading']
    start.caption=request.POST['edit_discription']
    start.range=request.POST['edit_range']
    start.save()
    return redirect("/starter")



# ---------------------(registraion)------------------------------


def registraion(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    r_Data=REGISTRATION.objects.all()
    obj={'r_Data':r_Data}
    return render(request,'admin/registraion.html',obj)

def save_admin_reg(request):
    if 'user_id' not in request.session: 
        return redirect("/admin/login")
    reg=REGISTRATION.objects.get(id=1)
    reg.name=request.POST['Name']
    reg.mobile=request.POST['mobile']
    reg.email=request.POST['email']
    reg.user_name=request.POST['username']
    reg.password=request.POST['password']
    reg.save()
    return redirect("/registraion")

 
def login(request):
    return render(request,'admin/login.html')

def save_login(request):
    l_data=REGISTRATION.objects.filter(
       user_name=request.POST['user_name'],
       password=request.POST['password'],
    )
    for i in l_data:
        request.session['user_id'] =i.id
        
    if(request.session.has_key('user_id')):
        return redirect("admin/")
    
    else:
        return redirect("/admin/login" )