from django.conf.urls import url, include
from .views import login,userin,logoutuser, requests, request_caller, request_acceptor,notification,request_accepted,free,request_free
urlpatterns=[
	url(r'^login/$',login),
	url(r'^userin/$',userin,name='userin'),
	url(r'^logout/$',logoutuser),
	url(r'^request/$', requests),
	url(r'^request_caller/$',request_caller),
	url(r'^request_acceptor/$',request_acceptor),
	url(r'^notification/$',notification),
	url(r'^request_accepted/$',request_accepted),
	url(r'^free/$',free),
	url(r'^request_free/$',request_free)
]