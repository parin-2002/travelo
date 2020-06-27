from django.shortcuts import render
from .models import destini

# Create your views here.
def index(request):
	obj1=destini.objects.all()
	return render(request,'index.html',{'data':obj1})
