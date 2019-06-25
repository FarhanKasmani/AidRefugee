from django.shortcuts import render
from .models import Camps, CampsItems, CampsFacl
from django.http import JsonResponse
from twilio.rest import Client
# Create your views here.

def home_page(request):
    return render(request, 'ngo/PAGE1(home).html', {})

def viewRefugees(request):
    return render(request, 'ngo/PAGE2(view).html', {'mylocation': False})

def viewRefugeeCamp(request):
    if request.is_ajax():
        myself = request.user
        if request.user.ngo:
            qs = Camps.objects.filter(user=myself)
        else:
            qs = Camps.objects.all()
        others = []
        for x in qs:
            if x != myself:
                contentString = '<div class="card" style="width: 18rem;"><img class="card-img-top" src=".../100px180/" alt="Card image cap"><div class="card-body"><h5 class="card-title">{name}</h5><p class="card-text"><b>Mobile</b>{mobile}</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div>'.format(name=x.name,mobile=x.name)
                t = {}
                if not request.user.ngo:
                    contentString += "<a class='btn btn-primary' href='/family/donate' role='button'>Donate/Receive</a>"
                t['contentString'] = contentString
                t['location'] = { 'lat': float(x.latitude), 'lng': float(x.longitude) }
                others.append(t)
        data = {"others": others}
        print(data)
        return JsonResponse(data)
    return render(request, 'ngo/PAGE4(CampDetails).html', {})

def placeRefugeeCamp(request):
    if request.is_ajax():
        print(request.POST)
        myself = request.user
        obj = Camps(
            user=myself,
            name=request.POST.get('name'),
            latitude=request.POST.get('lat'),
            longitude=request.POST.get('lng')
        )
        obj.save()
        account_sid = "TWILIO_ACCOUNT_SID"
        auth_token  = "TWILIO_ACCOUNT_AUTH_TOKEN"
        client = Client(account_sid, auth_token)
        client.messages.create(
            to='+919594860204',
            from_="+15709895673",
            body = "Hi this is Yashvi from "+request.POST.get('name')+". For any help contact +91-1234567899"
        )
        print(request.POST)
        for x in request.POST.get('items'):
            ob = CampsItems(camp=obj, items=x)
            ob.save()
        for x in request.POST.get('facs'):
            ob = CampsFacl(camp=obj, facl=x)
            ob.save()



    return render(request, 'ngo/PAGE3(PlaceCamp).html', {})
