from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from ngo.models import Camps
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    return render(request, "home_page.html", {})

def guest(request):
    print(request.POST)
    print(request.POST.get('name'))
    user = authenticate(request, username=request.POST.get('email'), password='ajay123')
    print(user)
    if user is not None:
        print(user)
        login(request, user)
        return redirect("/homepage")
    return render(request, "auth/guest_email.html", {})

def people(request):
    myself = request.user
    myd = {
        "full_name": myself.full_name,
        "mobile": myself.mobile_no,
        "lat": myself.latitude,
        "long": myself.longitude,
    }
    User = get_user_model()
    qs = User.objects.filter(ngo=False)
    others = []
    for x in qs:
        if x != myself:
            contentString = '<div class="card" style="width: 18rem;"><img class="card-img-top" src=".../100px180/" alt="Card image cap"><div class="card-body"><h5 class="card-title">{name}</h5><p class="card-text"><b>Mobile</b>{mobile}</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div>'.format(name=x.full_name,mobile=x.mobile_no)
            t = {}
            t['contentString'] = contentString
            t['location'] = { 'lat': float(x.latitude), 'lng': float(x.longitude) }
            others.append(t)
    qs = Camps.objects.all()
    for x in qs:
        contentString = '<div class="card" style="width: 18rem;"><img class="card-img-top" src=".../100px180/" alt="Card image cap"><div class="card-body"><h5 class="card-title">{name}</h5><p class="card-text"><b>Mobile</b>{mobile}</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div>'.format(name=x.name,mobile=x.name)
        t = {}
        t['contentString'] = contentString
        t['location'] = { 'lat': float(x.latitude), 'lng': float(x.longitude) }
        t['camps'] = 1
        others.append(t)

    if request.user.ngo == True:
        data = {"others": others}
    else:
        qs = Camps.objects.all()
        data = {"myself": myd, "others": others}
    if request.is_ajax:
        return JsonResponse(data)
    return render(request, "home_page.html", data)

def updateLatLong(request):
    if request.is_ajax:
        user = request.user
        print(request.POST)
        user.latitude = request.POST.get('lat')
        user.longitude = request.POST.get('lng')
        user.save()
        return JsonResponse({"Success": "done"})

def donate(request):
    return render(request, "searchFamily/donate-receive.html", {})
