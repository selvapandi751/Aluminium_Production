from django.shortcuts import render,HttpResponse,redirect
from .models import Datas
# Create your views here.

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address')
        mail=request.POST.get('mail')
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj = Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Mail=mail
        obj.Username=username
        obj.Password=password
        obj.save()

    return render(request,'register.html')

def userlog(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            Datas.objects.get(Username = username,Password = password)
            return redirect('homepage')
        except:
            return HttpResponse('invalid username and password')



        
       
       
    return render(request,'index.html')

def adminlog(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        if username=="admin" and password =='admin':
            return redirect('adminhome')
        else:
            return HttpResponse('Invalid admin')
    return render(request,'adminlog.html')

def adminhome(request):
    return render(request,'adminhome.html')

def pending_details(request):
    datas = Datas.objects.filter(Status=0)

    return render(request,'pending_details.html',{'datas':datas})

def approved_details(request):
    datas = Datas.objects.filter(Status = True)

    return render(request,'approved_details.html',{'datas':datas})

def approve(request,id):
    data = Datas.objects.get(id=id)
    data.Status=True
    data.save()
    return redirect('pending_details')

def dissmiss(request,id):
    data = Datas.objects.get(id=id)
    data.Status=False
    data.save()
    return redirect('approved_details')

def homepage(request):
    if request.method=='POST':
        bauxite = request.POST.get('bauxite')
        percentage = request.POST.get('percentage')

        bauxiteval = int(bauxite)
        percentageval = int(percentage)

        mass_al2o3 = percentageval/100*bauxiteval
        mass_al2o3val = float(mass_al2o3)

        mass_AL_gm = 54/102*mass_al2o3val*1000
        mass_AL_gm_val = float(mass_AL_gm)
        mass_AL_kg = mass_AL_gm_val/1000
        mass_AL_kg_int = float(mass_AL_kg)

        if mass_AL_kg_int==0:
            val = "Empty"
            return render(request,'homepage.html',{'val':val})
        elif(mass_AL_kg_int>0 and mass_AL_kg_int<1):
            mass_AL_g = mass_AL_kg_int*1000
            return render(request,'homepage.html',{'mass_AL_g': mass_AL_g})
        else:
            return render(request,'homepage.html',{'mass_AL_kg': mass_AL_kg})

        
    return render(request,'homepage.html')

def calculation(request):
    return render(request,"calculation.html")