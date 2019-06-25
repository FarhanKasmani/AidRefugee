from django.shortcuts import render

from .models import LostPeople
# Create your views here.
def findPeople(request):
    print(request.FILES)
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        m = ExampleModel.objects.get(pk=course_id)
        m.model_pic = form.cleaned_data['image']
        m.save()
        return HttpResponse('image upload success')
    return render(request, 'lost/upload.html')
