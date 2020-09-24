from django.http import HttpResponse
from django.shortcuts import redirect, render

from photobazaarapp.models import Category, Image


# Create your views here.
def index(request):
   images = Image.objects.all()
   cat = Category.objects.all()
   data={
        'images':images,
        'cat':cat
   }

   return render(request,'index.html',data)

def show_category(request,cid):
  
   cat = Category.objects.all()

   category=Category.objects.get(pk=cid)

   images = Image.objects.filter(cat=category)
   data={
        'images':images,
        'cat':cat
   }

   return render(request,'index.html',data)

def home(request):
     return redirect('/home')
