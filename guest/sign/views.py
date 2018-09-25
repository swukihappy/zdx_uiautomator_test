from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
	return render(request,"index.html")
def sigin(request):
	return render(request,"sigin.html")
def login_action(request):
	if request.method=="POST":
		username=request.POST.get("username","")
		password=request.POST.get("password","")
		if username=="zdx" and password=="123456":
			return HttpResponseRedirect("/event_manage/")
		else:
			#return HttpResponse("-1")
			return render(request,'sigin.html',{'error':"username or password error"}) 
	return render(request,"sigin.html")
def event_manage(request):
	return render(request,"event_manage.html")