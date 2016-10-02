from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Users, Books
from .forms import Form, Books_Form, Search_Form
# Create your views here.

objects=None
objects1=None
objects2=None
def login(request):
	# print request.user 
	return render(request,"login.html",{'request':request})
@login_required
def userin(request):
	global objects 
	objects = None
	objects1=None
	objects2=None
	# user_list = request.user.social_auth.values_list('uid')
	# print user_list
	user=request.user.social_auth.values_list('uid')[0][0]
	# objects=User.objects.all()
	
	try:
		uid = Users.objects.get(uid=user)
	except Users.DoesNotExist:
		uid = None

	if uid is not None:
		if request.method == 'POST':
			form = Books_Form(request.POST)
			if form.is_valid():
				# messages=False
				cd = form.cleaned_data
				name = cd['name']
				author = cd['author']
				rid = '0'
				newdata = Books(name=name,author=author,uid=user,rid=rid,available='1')
				newdata.save()
				messages.success(request,'Successfully updated to your database')
				# messages=True
		else:
			form=Books_Form()
		return render(request,"homepage.html",{'form':form})
	else:
		if request.method == 'POST':

	
			form = Form(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				name = cd['name']
				phone_number = cd['phone_number']
				description = cd['description']
				newdata = Users(name=name,phone_number=phone_number, description=description, uid=user)
				newdata.save()
		else:
			form=Form()
		return render(request,'personalInformation.html', {'form': form})
@login_required
def logoutuser(request):
	logout(request)
	return HttpResponseRedirect('/book_share/login')
@login_required
def requests(request):
	global objects
	if request.method=='POST':
		form=Search_Form(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			name = cd['text']
			print name
			objects=Books.objects.filter(name=name,rid='0',available='1')

			print objects
	else:
		form=Search_Form()
	return render(request,'requests.html',{'form':form,'objects':objects})
@login_required
def request_caller(request):
	global objects
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	print user_uid
	print objects
	for obj in objects:
		print obj.name
		print obj.rid
		print obj.available
		obj.rid=user_uid
		obj.available='0'
		obj.save()
		print obj.rid
		print obj.available
	# lender_uid=objects[0]['uid']
	# name=request.GET['name']
	# print name
	# lender_uid=request.GET['uid']
	# print lender_uid
	# objects=Books.objects.filter(uid=lender_uid,name=name)
	# print objects
	# objects.update(rid=user_uid,available=0)
	# print objects

	return HttpResponseRedirect('/book_share/userin/')
@login_required
def request_acceptor(request):
	global objects1
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	print user_uid
	try:
		objects1=Books.objects.filter(available='0',uid=user_uid)
	except Users.DoesNotExist:
		objects1 = None
	
	print objects1
	return render(request,'request_acceptor.html',{'objects1':objects1})
@login_required
def request_accepted(request):
	global objects1
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	for obj in objects1:
		print obj.name
		print obj.rid
		print obj.available
		obj.available='2'
		obj.save()
		print obj.rid
		print obj.available
	return HttpResponseRedirect('/book_share/request_acceptor/')
@login_required
def notification(request):
	global objects2
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	objects2=Books.objects.filter(rid=user_uid,available='2')
	print objects2
	return render(request,"notification.html",{'objects2':objects2})
@login_required
def free(request):
	global objects
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	# if request.method=='POST':
		# form=Search_Form(request.POST)
		# if form.is_valid():
			# cd = form.cleaned_data
			# name = cd['text']
			# print name
	objects=Books.objects.filter(uid=user_uid,available='2')

	print objects
	# else:
		# form=Search_Form()
	return render(request,'free.html',{'objects':objects})
@login_required
def request_free(request):
	global objects
	user_uid=request.user.social_auth.values_list('uid')[0][0]
	for obj in objects:
		print obj.name
		print obj.rid
		print obj.available
		obj.available='1'
		obj.rid='0'
		obj.save()
		print obj.rid
		print obj.available
	return HttpResponseRedirect('/book_share/free/')
