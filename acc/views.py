from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
	if(request.method=='POST'):
		fname=request.POST['fname']
		lname=request.POST['lname']
		user=request.POST['username']
		email=request.POST['email']
		pas=request.POST['password']
		cpas=request.POST['cpassword']
		print(fname,email)
		
		if(pas==cpas):
			if User.objects.filter(username=user).exists():
				messages.info(request,'user taken')
				return render(request,'register.html')
				
			if User.objects.filter(email=email).exists():
				messages.info(request,'email is alradey exists')
				return redirect("register")
				
			else:
				user=User.objects.create_user(user,email,pas)
				user.last_name=lname
				user.first_name=fname
				user.save()
				print('user created')
				return redirect('login')
		else:
			messages.info(request,'password not sem')
			return render(request,'register.html')
	else:
		return render(request,'register.html')

def login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'plase register and after try to login')
			return redirect("login")	
	else:
		return render(request,'login.html')
		
def logout(request):
	auth.logout(request)
	return redirect("/")
		
