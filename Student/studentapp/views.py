from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Hello world")
#
# def showdetails(request):
#     code="<html><body><h1>Welcome to Django</h1><h3>Hello Bewqoof</h3></body></html>"
#     return HttpResponse(code)
#

# def show(request):
#     return render(request, "main.html",{"name":"Sathya Details"})
#
# def show(req):
#     details={"idno":101, "name":"satya", "salary":125000.00}
#     return render(req,"main.html",{"data":details})

# def showindex(req):
#     d1={101:{"name":"Ravi","salary":125000.00},102:{"name":"kumar","salary":150000.00},103:{"name":"mohan","salary":100000.00}}
#     return render(req,"index.html",{"data":d1})

from studentapp.models import Details

def showdetails(request):
    return render(request,"index.html")

def details(request):
    idno=request.POST.get("txtid")
    name=request.POST.get("txtname")
    sal=request.POST.get("txtsal")
    exp=request.POST.get("txtexp")
    des=request.POST.get("txtdes")
    e1=Details(idno=idno,name=name,salary=sal,exp=exp,designation=des)
    e1.save()
def display(request):
    qs=Details.objects.all()
    return render(request,"viewall.html",{"data":qs})
