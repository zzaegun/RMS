from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from datetime import datetime  

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
    fin_items = T_ORDER_INFO.objects.all().filter(ORDER_FIN = 1)
    if fin_items.count() != 0:
	    last_item = fin_items.latest('ORDER_ID')
    else:
	    last_item = 0
	    last_available = False

    item = T_ORDER_INFO.objects.all().get(pk=request.POST['item'])

    proc = item.ITEM_ID.PROCESS_ID.SUBPROC_ORDER
    subproc = T_SUB_PROCESS.objects.all()
    
    proc_array = proc.split(',')
    return render(request, 'c2_1.html', {'last_available': last_available, 'sprc_list': subproc, 'last_val': last_item, 'now_val': item, 'subprc': proc_array})

def aPurMan2(request):
    item = T_ORDER_INFO.objects.all().get(pk=request.POST['item'])
    proc = item.ITEM_ID.PROCESS_ID.SUBPROC_ORDER
    subproc = T_SUB_PROCESS.objects.all()
    proc_array = [int(i) for i in proc.split(',')]
    return render(request, 'c2_2.html', {'now_val': item, 'subprc': proc_array, 'sprc_list': subproc})


def aPurMan3(request):
    item = T_ORDER_INFO.objects.all().get(pk=request.POST['item'])
    proc = item.ITEM_ID.PROCESS_ID.SUBPROC_ORDER
    subproc = T_SUB_PROCESS.objects.all()
    proc_array = [int(i) for i in proc.split(',')]
    machine = T_MACHINE_STATUS.objects.all()

    #get selected machine number
    selected = []
    for i in proc_array:
        st = machine.get(pk=i).MACHINE_SCHED
        lt = machine.get(pk=i).MACHINE_LT
        et = st + timezone.timedelta(minutes = lt)
        selected.append({'subprc': i, 'machine': request.POST['sel_sp_'+str(i)], 'start_time':st, 'end_time':et})

    return render(request, 'c2_3.html', {'now_val': item, 'subprc': proc_array, 'sprc_list': subproc, 'machine_info': selected})

def admin1(request):
    schedules = T_PROD_SCHEDULE.objects.all()
    
    for schedule in schedules:
        name, start_time, end_time, chain, end_flag = calculate(schedule.SCHEDULE_ID)
        #machine = schedule.MACHINE_USE.split(',')
        schedule.MACHINE = []
        for i, v in enumerate(start_time):
            schedule.MACHINE.append({'name': name[i],'start_time':start_time[i],'end_time':end_time[i], 'chain':chain[i], 'end_flag':end_flag[i]})

    return render(request, 'd1.html', {'schedules': schedules})

def admin2(request):
    return render(request, 'd2.html', {})

def calculate(num):
    schedule = T_PROD_SCHEDULE.objects.get(pk=num)
    use = schedule.MACHINE_USE
    name = []
    start_time = []
    end_time = []
    chain = []
    end_flag = []

    tmp = schedule.PROD_START

    for i in use.split(','):
        if i.find('-') != -1:
            max_prod_time = 0
            for j in i.split('-'):
                start_time.append(tmp)
                m = T_MACHINE_STATUS.objects.get(pk=j)
                name.append(m.MACHINE_NAME)
                tmp2 = tmp + timezone.timedelta(minutes = m.MACHINE_LT)
                end_time.append(tmp2)
                chain.append(True)

                #check max production time
                if max_prod_time < m.MACHINE_LT:
                    max_prod_time = m.MACHINE_LT

                if i.index(j) == len(i)-1:
                    end_flag.append(True)
                    tmp = tmp+timezone.timedelta(minutes = max_prod_time)
                else:
                    end_flag.append(False)
        
        else:
            start_time.append(tmp)
            m = T_MACHINE_STATUS.objects.get(pk=i)
            name.append(m.MACHINE_NAME)
            tmp = tmp + timezone.timedelta(minutes = m.MACHINE_LT)
            end_time.append(tmp)
            chain.append(False)
            end_flag.append(False)

    print(chain)
    return name, start_time, end_time, chain, end_flag


def notwk(request):
    machines = T_MACHINE_STATUS.objects.all()

    schedules = T_PROD_SCHEDULE.objects.all()
    for machine in machines:
        result = []
        for schedule in schedules:
            #print(machine.MACHINE_ID, schedule.MACHINE_USE.split(','))
            if str(machine.MACHINE_ID) in schedule.MACHINE_USE.split(','):
                result.append(schedule.SCHEDULE_ID)
        
        machine.MACHINE_RELATED = result

    return render(request, 'd3.html', {'machines': machines, 'schedules': schedules})





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
    new_prod_type = T_PROD_TYPE.objects.get(pk=item)
    

    #확약주문에 대해서 아래의 sequence 따른다.
    if mod.ORDER_FIN == True:
        prod_modify = T_PROD_SCHEDULE.objects.get(ORDER_ID=order)

        #기존 아이템과 달라지는 경우 -> 레이아웃 변경
        if int(item) != int(mod.ITEM_ID.ITEM_ID):
            print("기존 아이템과 달라지는 경우")
            subproc = new_prod_type.PROCESS_ID.SUBPROC_ORDER
            prod_modify.PROCESS_ID = T_PROD_TYPE.objects.get(pk=item).PROCESS_ID

            machine = []

            for s in subproc.split(','):
                if s.find('-') != -1:
                    subm = []
                    for s_ in s.split('-'):
                        m_no = T_MACHINE_STATUS.objects.filter(MACHINE_ENABLED=1).filter(SUBPROC_ID=s)
                        for m_sep in m_no:
                            if prod_modify.MACHINE_USE.find(m_sep.MACHINE_ID) != -1: 
                                m_str = m_sep.MACHINE_ID
                        subm.append(str(m_str))
                    subm_str = '-'.join(subm)
                    machine.append(subm_str)
                else:
                    m_no = T_MACHINE_STATUS.objects.filter(MACHINE_ENABLED=1).filter(SUBPROC_ID=s)
                    for m_sep in m_no:
                        if prod_modify.MACHINE_USE.find(str(m_sep.MACHINE_ID)) != -1: 
                            m_str = m_sep.MACHINE_ID
                    machine.append(str(m_str))
                    print(machine)
            
            prod_modify.MACHINE_USE = ','.join(machine)

        #수량이 달라지는 경우 -> 생산량 조정
        elif int(num) > int(mod.ORDER_QTY):
            print("수량이 달라지는 경우")
            subproc = new_prod_type.PROCESS_ID.SUBPROC_ORDER
            machine = []
            capa = {}

            for s in subproc.split(','):
                if s.find('-') != -1:

                    continue
                else:  
                    m_no = T_MACHINE_STATUS.objects.filter(MACHINE_ENABLED=1).filter(SUBPROC_ID=s)
                    val = 0
                    for m_sep in m_no:
                        val += m_sep.MACHINE_CAPA

                    print("주문비교: ", val, num)
                    #주문량이 한개보다는 크고 두개보다는 작을 때
                    if val < num:
                        print("개발중")
                    #원래는 주문량이 아예 초과하면 오류를 return해야 함
                    
    
    prod_modify.save()
    
    mod.ORDER_QTY = num
    mod.ITEM_ID = new_prod_type
    mod.save()
    
    return HttpResponseRedirect(reverse('main:cList'))

def notwk_setUnabled(request):
    item = request.POST['item']
    m = T_MACHINE_STATUS.objects.get(pk=item)
    m.MACHINE_ENABLED = 0
    m.save()
    return HttpResponseRedirect(reverse('main:notwk'))

def notwk_setEnabled(request):
    item = request.POST['item']
    m = T_MACHINE_STATUS.objects.get(pk=item)
    m.MACHINE_ENABLED = 1
    m.save()
    return HttpResponseRedirect(reverse('main:notwk'))

def notwk_selectAlternate(request):
    #adding..
    print(request.POST['old'], request.POST['item'])
    return HttpResponseRedirect(reverse('main:notwk'))

def aPurMan3_addSchedule(request):
    machine = request.POST['machine']
    order_no = request.POST['order_no']
    start_time = request.POST['start_time'].replace(u'오전','am').replace(u'오후','pm')
    end_time = request.POST['end_time'].replace(u'오전','am').replace(u'오후','pm')

    print(start_time, end_time)
    order = T_ORDER_INFO.objects.get(pk=order_no)

    T_PROD_SCHEDULE.objects.create(
        PROD_START = start_time,
        PROD_END = end_time,
        MACHINE_USE = ''.join([str(i) for i in machine]),
        MACHINE_QTY = order.ORDER_QTY,
        ORDER_ID = order,
        PROCESS_ID = order.ITEM_ID.PROCESS_ID,
    )

    order.ORDER_FIN = 1
    order.save()

    return HttpResponseRedirect(reverse('main:admin1'))

