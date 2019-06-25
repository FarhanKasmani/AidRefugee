from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

from .models import Family

class FamilyListView(ListView):
    template_name = "searchFamily/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FamilyListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        User = get_user_model()
        if query is not None:
            lookups = Q(full_name__icontains=query) & Q(ngo=False)
            return User.objects.filter(lookups).distinct()
        return User.objects.all()

# def family_list_view(request):
#     queryset = Family.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, "searchFamily/list.html", context)

class FamilyDetailView(DetailView):
    queryset = Family.objects.all()
    template_name = "searchFamily/detail.html"
    User = get_user_model()

    def get_context_data(self, *args, **kwargs):
        context = super(FamilyDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = self.User.objects.get_by_id(pk)
        try:
            instance = self.User.objects.get(slug=slug)
        except self.User.DoesNotExist:
            raise Http404("Not found")
        except:
            raise Http404("Areereee")
        return instance

class SearchUserView(ListView):
    template_name = "searchFamily/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def addMember(request):
    uid = request.POST.get('user_id')

    return render(request, 'searchFamily/list.html', {})

def familyMap(request):
    return render(request, 'searchFamily/familyMap.html', {})

def getFamilyData(request):
    print("JJJJ")
    myself = request.user
    myd = {
        "full_name": myself.full_name,
        "mobile": myself.mobile_no,
        "lat": myself.latitude,
        "long": myself.longitude,
    }
    User = get_user_model()
    qs = Family.objects.filter(user=myself)
    others = []
    for x in qs:
        if x != myself:
            contentString = '<div class="card" style="width: 18rem;"><img class="card-img-top" src=".../100px180/" alt="Card image cap"><div class="card-body"><h5 class="card-title">{name}</h5><p class="card-text"><b>Mobile</b>{mobile}</p><a href="#" class="btn btn-primary">Go somewhere</a></div></div>'.format(name=x.family_members.full_name,mobile=x.family_members.mobile_no)
            t = {}
            t['contentString'] = contentString
            t['location'] = { 'lat': float(x.family_members.latitude), 'lng': float(x.family_members.longitude) }
            others.append(t)
    data = {"myself": myd, "others": others}
    if request.is_ajax:
        return JsonResponse(data)
    return render(request, "searchFamily/myfamily.html", {})

def getRefugee(request):
    pass

def adddonate(request):
    print(request.POST)
    return render(request, 'home_page.html')

def donate(request):
    print("KKKK")
    return render(request, 'searchFamily/donate-receive.html', {})
