from django.shortcuts import render,redirect
from .models import User,Elite,Pre,Nor,Bus
from .forms import UserForm,LoginForm,EliteForm,PreForm,NorForm
from django.http import HttpResponse
def func_1(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            global category,pid,pname           
            category=request.POST.get('category')
            pname=request.POST.get('Passenger_name')
            pid=request.POST.get('pid')
        return redirect('/login')
    return render(request,'home.html',{'form':form})

l=[]
def el(request,pid,pname):
    form=EliteForm()
    pid=pid
    pname=pname
    if request.method=='POST':
        form=EliteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            sou=request.POST.get('source')
            bo=request.POST.get('bus_no')
            de=request.POST.get('destination')
            d=request.POST.get('depature')
            ca=request.POST.get('category')
            se=request.POST.get('seat_no')
            rms=request.POST.get('seat_no')
            if rms not in l:
                l.append(rms)
                return render(request,'elreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
            else:
                return render(request,'f.html')
        return render(request,'elreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
    return render(request,'el.html',{'form':form,'pid':pid,'pname':pname})

l1=[]
def pr(request,pid,pname):
    form=PreForm()
    if request.method=='POST':
        form=PreForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            sou=request.POST.get('source')
            bo=request.POST.get('bus_no')
            de=request.POST.get('destination')
            d=request.POST.get('depature')
            ca=request.POST.get('category')
            se=request.POST.get('seat_no')
            rms=request.POST.get('seat_no')
            if rms not in l1:
                l1.append(rms)
                return render(request,'prreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
            else:
                return render(request,'f.html')
        return render(request,'prreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
    return render(request,'pr.html',{'form':form,'pid':pid,'pname':pname})

l2=[]
def no(request,pid,pname):
    form=NorForm()
    if request.method=='POST':
        form=NorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            sou=request.POST.get('source')
            bo=request.POST.get('bus_no')
            de=request.POST.get('destination')
            d=request.POST.get('depature')
            ca=request.POST.get('category')
            se=request.POST.get('seat_no')
            rms=request.POST.get('seat_no')
            if rms not in l2:
                l2.append(rms)
                return render(request,'noreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
            else:
                return render(request,'f.html')
           
        return render(request,'noreceipt.html',{'sou':sou,'bo':bo,'de':de,'d':d,'ca':ca,'pname':pname,'se':se,'rms':rms,'pid':pid})
    return render(request,'no.html',{'form':form,'pid':pid,'pname':pname})

def login_view(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            res=User.objects.filter(username=username,password=password)
            #return HttpResponse("ok")
            if res:
                for i in res:

                    if i.category=='Elite':
                        pid=i.pid
                        pname=i.Passenger_name
                        return redirect(el,pid,pname)
                    elif i.category=='Premium':
                        pid=i.pid
                        pname=i.Passenger_name
                        return redirect(pr,pid,pname)
                    else:
                        pid=i.pid
                        pname=i.Passenger_name
                        return redirect(no,pid,pname)
            else:
                render(request,'login.html',{'msg':'invalid'})
        else:
            return render(request,'login.html',{'form':form})
    else:
        return render(request,'login.html',{'form':form})