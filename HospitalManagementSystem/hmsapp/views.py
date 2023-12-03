from django.shortcuts import redirect, render
from django.http import HttpResponse
# import models
from hmsapp.models import appointment 
#    appname.models       classname
# Create your views here.
def home(request):
    return render(request,'index.html') 

def gotoappointment(request):
    return render(request,'appointment.html')

# CREATE operation
def makeappointment(request):
    if request.method=='POST':
    #   variable=request.POST.get('namefromhtmldocument')
        firstName=request.POST.get('firstname')
        lastName=request.POST.get('lastname')
        agevalue=request.POST.get('age')
        datevalue=request.POST.get('doa')
        appointmentdata=appointment(fname=firstName, lname=lastName, age=agevalue, date=datevalue)
        appointmentdata.save()
    return redirect("/viewdetails")

# READ operation
def displayOperation(request):
    patient=appointment.objects.all()
    return render(request,'CRUDOperations.html',{'patient':patient})

# #UPDATE operation
def editPage(request,id):
    edit=appointment.objects.get(pk=id)
    return render(request,'update.html',{"edit":edit})

def updateOperation(request,id):
    ufname=request.POST.get('firstname')
    ulname=request.POST.get('lastname')
    uage=request.POST.get('age')
    presentData=appointment.objects.get(pk=id)
    presentData.fname=ufname
    presentData.lname=ulname
    presentData.age=uage
    presentData.save()
    return redirect("/viewdetails")

# DELETE operation
def deleteOperation(request,id):
    patientd=appointment.objects.get(pk=id)
    patientd.delete()
    return redirect("/viewdetails")