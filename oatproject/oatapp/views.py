from django.shortcuts import render
from django.http import HttpResponse
from .models import person
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def gallery(request):
    return render(request,"gallery.html")
def contact(request):
    return render(request,"contact.html")
def form(request):
    return render(request,"form.html")
def Person(request):
    all_person = person.objects.all()
    return render(request, 'person.html',{'all_person'   :all_person })