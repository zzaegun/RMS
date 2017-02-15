from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

# Create your views here.
def test(request): #login and test
	return render(request, 'tpage.html', {})

def login(request): #login and test
	return render(request, 'login.html', {})

def cReq(request):
    items = T_PROD_TYPE.objects.all()
    
    #comparing phase
    if T_ORDER_INFO.objects.all().count() != 0:
        last_order = T_ORDER_INFO.objects.latest('ITEM_ID') #earliest
    else:
        last_order = 0
    
    template = 'b1.html'
    return render(request, template, {'items': items, 'last_order': last_order, 'new_order': last_order+1})

def cReq_newRequest(request):
    item = request.POST['item']
    num = request.POST['num']
    order_date = timezone.now()
    print(item, num, order_date) #주문수량, 주문제품번호
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
