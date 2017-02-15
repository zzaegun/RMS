from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
def test(request): #login and test
	return render(request, 'tpage.html', {})

def login(request): #login and test
	return render(request, 'login.html', {})

def cReq(request):
	items = T_PROD_TYPE.objects.all()
	template = 'b1.html'
	return render(request, template, {'items': items})

def cReq_newRequest(request):
	item = request.POST['item']
	num = request.POST['num']
	print(item, num)
	return HttpResponseRedirect(reverse('main:cList'))

def cList(request):
	return render(request, 'b2.html', {})

def cModify(request):
	return render(request, 'b3.html', {})

def aPur(request):
	return render(request, 'c1.html', {})

def aPurMan1(request):
	return render(request, 'c2_1.html', {})

def aPurMan2(request):
	return render(request, 'c2_2.html', {})

def aPurMan3(request):
	return render(request, 'c2_3.html', {})

def admin1(request):
    return render(request, 'd1.html', {})

def admin2(request):
    return render(request, 'd2.html', {})
    
def notwk(request):
    return render(request, 'd3.html', {})
