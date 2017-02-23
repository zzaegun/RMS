from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

def get_latest_order_no():
    #comparing phase
    if T_ORDER_INFO.objects.all().count() != 0:
        return T_ORDER_INFO.objects.latest('ORDER_ID').ORDER_ID #earliest
    else:
        return 0
        
# Create your views here.
def test(request): #login and test
	return render(request, 'tpage.html', {})

def login(request): #login and test
	return render(request, 'login.html', {})

def cReq(request):
    items = T_PROD_TYPE.objects.all()
    
    #comparing phase
    last_order = get_latest_order_no()
    
    template = 'b1.html'
    return render(request, template, {'items': items, 'last_order': last_order, 'new_order': last_order+1})

def cList(request):
    lists = T_ORDER_INFO.objects.all()
    return render(request, 'b2.html', {'lists': lists})

def cModify(request):
	items = T_PROD_TYPE.objects.all()
	item = T_ORDER_INFO.objects.all().get(pk=request.POST['item'])
	return render(request, 'b3.html', {'items': items, 'val': item})

def aPur(request):
	lists = T_ORDER_INFO.objects.all()
	return render(request, 'c1.html', {'lists': lists})

def aPurMan1(request):
	last_available = True
	fin_items = T_ORDER_INFO.objects.all().filter(ORDER_FIN = True)
	if fin_items.count() != 0:
		last_item = fin_items.latest('ORDER_ID').ORDER_ID
	else:
		last_item = 0
		last_available = False

	item = T_ORDER_INFO.objects.all().get(pk=request.POST['item'])
	proc = item.ITEM_ID.PROCESS_ID.SUBPROC_ORDER
	proc_array = proc.split(',')
	return render(request, 'c2_1.html', {'last_available': last_available, 'last_val': last_item, 'now_val': item, 'subprc': proc_array})

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





############## LOGICAL
def cReq_newRequest(request):
    """
    	ORDER_ID = models.IntegerField(db_index=True, primary_key=True)
	ORDER_DATE = models.IntegerField(default = 0)
	ITEM_ID = models.ForeignKey(T_PROD_TYPE, on_delete=models.CASCADE)
	ORDER_QTY = models.IntegerField(default = 0)
	ORDER_FIN = models.DateTimeField(default = True)
    FIN_TIME = models.DateTimeField(null=True)
    """
    
    item = request.POST['item']
    num = request.POST['num']
    order_id = get_latest_order_no() + 1
    order_date = timezone.now()
    prod = T_PROD_TYPE.objects.get(pk=item)
    
    prod.t_order_info_set.create(
        ORDER_ID = order_id,
        ORDER_DATE = order_date,
        ITEM_ID = item,
        ORDER_QTY = num,
        ORDER_FIN = False,
    )
    print(item, num, order_date) #주문수량, 주문제품번호
    
    return HttpResponseRedirect(reverse('main:cList'))

def cModify_Request(request):
    order = request.POST['ord']
    item = request.POST['item']
    num = request.POST['num']
    mod = T_ORDER_INFO.objects.get(pk=order)
    
    mod.ORDER_QTY = num
    mod.ITEM_ID = T_PROD_TYPE.objects.get(pk=item)
    
    mod.save()
    return HttpResponseRedirect(reverse('main:cList'))
    