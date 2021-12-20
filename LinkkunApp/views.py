from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Link

# Create your views here.
def index(request):
	return render(request, 'index.html')

def home(request, cred):
	links = Link.objects.filter(cred=cred)
	total = len(links)
	return render(request, 'home.html', {'links':links, 'total':total})

def signup(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		''' Password validation '''
		if password1 == password2:
			if User.objects.filter(email=email).exists():
				''' Email validation '''
				messages.info(request, 'Email already used.')
				return redirect('/')
			elif User.objects.filter(username=username).exists():
				''' Username validation '''
				messages.info(request, 'Username already used.')
				return redirect('/')
			else:
				''' Register new user '''
				new_user = User.objects.create_user(email=email, username=username, password=password1)
				new_user.save()
				''' Auto logged in '''
				user = auth.authenticate(username=username, password=password1)
				auth.login(request, user)
				return redirect('/'+str(user.id)+'/?username='+username)
		else:
			messages.info(request, 'Password does not match.')
			return redirect('/')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		''' User validation '''
		user = auth.authenticate(username=username, password=password)
		if user != None:
			auth.login(request, user)
			return redirect('/'+str(user.id)+'/?username='+username)
		else:
			messages.info(request, 'Credentials invalid.')
			return redirect('/')

def logout(request, cred):
	auth.logout(request)
	return redirect('/')

def add(request, cred):
	if request.method == 'POST':
		name = request.POST['name']
		urls = request.POST['urls']
		cred = request.POST['cred']
		username = request.POST['username']
		''' Name validation '''
		if Link.objects.filter(name=name, cred=str(cred)).exists():
			messages.info(request, 'ERROR: Name already exists.')
		else:
			new_link = Link.objects.create(name=name, urls=urls, cred=str(cred))
			new_link.save()
		return redirect('/'+str(cred)+'/?username='+username)

def delete(request, cred):
	if request.method == 'POST':
		name = request.POST['name']
		cred = request.POST['cred']
		username = request.POST['username']
		''' Name validation '''
		if Link.objects.filter(name=name).exists():
			link = Link.objects.filter(name=name)
			link.delete()
		else:
			messages.info(request, 'ERROR: Link not found.')
		return redirect('/'+str(cred)+'/?username='+username)