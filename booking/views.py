from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'login.html')

user1=''
def logins(request):
    try:
        global user1,ids,name
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=customer.objects.filter(name=username).values()
        name=user[0]['name']
        if user[0]['password']==password:
            user1=name
            flights=flightdeatils.objects.all().values()
            return render(request,'Bookings.html',{'details':flights})
        else:
            return index(request)
    except Exception as e:
        return index(request)
    

def register(request):
    try:
        name=request.POST['name']
        password=request.POST['password']
        confirmation=request.POST['confirmation']
        email=request.POST['email']
        names=customer.objects.values_list('name')
        if name!='' and password==confirmation and name not in names[0]:
            user=customer(name=name,password=password,email=email)
            user.save()
        return render(request,"login.html")
    except:
        return render(request,'login.html')
    
def book(request):
    try:
        global user1
        id=request.POST.getlist('id')
        tic=request.POST.getlist('tickets')
        d={}
        j=0
        for i in tic:
            if i=='':
                continue
            d[id[j]]=i
            j+=1
        j=0
        for i in id:
            flight=flightdeatils.objects.get(id=i)
            f4=flightbookings.objects.filter(refno=flight.refno).exists()
            print(f4)
            if f4==False:
                flight2=flightbookings.objects.create(user=user1,refno=flight.refno,name=flight.name,time=flight.time,fromp=flight.fromp,top=flight.top,date=flight.date,seats=d[i])
                flight2.save()
            else:
                f3=flightbookings.objects.get(refno=flight.refno)
                print(f3)
                val1=f3.seats
                setattr(f3,'seats',val1+int(d[i]))
                f3.save()
            val=flight.seats
            t=d[i]
            setattr(flight, "seats", (val-int(t)))
            j+=1
        flight.save()
        return viewtickets(request)
    except Exception as e:
        print(e)
        flights=flightdeatils.objects.all().values()
        return render(request,'Bookings.html',{'details':flights})

def search(request):
    fn=request.POST['flightName']
    fp=request.POST['fromPlace']
    tp=request.POST['toPlace']
    t=request.POST['time']
    d=request.POST['date']
    if d=="":
        d=None
    if fn=='':
        fn=None
    if tp=='':
        tp=None
    if t=='':
        t=None
    if fp=='':
        fp=None
    flights=flightbookings.objects.filter(Q(name=fn) | Q(time=t) | Q(fromp=fp) | Q(top=tp) | Q(date=d)).values()
    return render(request,'Bookings.html',{'details':flights})


def search2(request):
    fn=request.POST['flightName']
    fp=request.POST['fromPlace']
    tp=request.POST['toPlace']
    t=request.POST['time']
    d=request.POST['date']
    if d=="":
        d=None
    if fn=='':
        fn=None
    if tp=='':
        tp=None
    if t=='':
        t=None
    if fp=='':
        fp=None
    flights=flightdeatils.objects.filter(Q(name=fn) | Q(time=t) | Q(fromp=fp) | Q(top=tp) | Q(date=d)).values()
    return render(request,'viewticket.html',{'details':flights})


def viewtickets(request):
    global user1
    print(user1)
    flight=flightbookings.objects.filter(user=user1).values()
    return render(request,'viewticket.html',{'details':flight,'user':user1})
