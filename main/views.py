from django.shortcuts import render

# Create your views here.
def test(request): #login and test
	return render(request, 'tpage.html', {})

def login(request): #login and test
	return render(request, 'login.html', {})

def cReq(request):
	return render(request, 'b1.html', {})

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