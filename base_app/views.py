import os
from django. contrib import messages
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render, redirect
from base_app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from io import BytesIO
from django.core.files import File
from django.conf import settings
import qrcode
from django.conf import settings
import random
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# import qrcode.image.svg
# from io import BytesIO
# from django.views.generic import View
# # from xhtml2pdf import pisa
# # from coreapp.utils import render_to_pdf ,get_template
# from django.db.models import Q
# import os


# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

# Create your views here.
def login(request):
    
    des = designation.objects.get(designation='trainingmanager')
    des1 = designation.objects.get(designation='trainer')
    des2 = designation.objects.get(designation='trainee')
    design3=designation.objects.get(designation="manager")
    design1=designation.objects.get(designation="developer")
    design2=designation.objects.get(designation="project manager")
    design4=designation.objects.get(designation="team leader")
    Adm1=designation.objects.get(designation="Admin")
    design=designation.objects.get(designation="tester")
    if request.method == 'POST':
        
       
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des.id).exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernametm'] = member.designation_id
            request.session['usernametm1'] = member.fullname
            request.session['usernametm2'] = member.id
            #request.session['usernamehr2'] = member.branch
            return render(request, 'dashsec.html', {'member': member})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des1.id).exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernametrnr'] = member.designation_id
            request.session['usernametrnr1'] = member.fullname
            request.session['usernametrnr2'] = member.team_id
            request.session['usernametrnr2'] = member.id
            return render(request, 'trainersec.html', {'member': member})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'], designation_id=des2.id).exists():
            member = user_registration.objects.get(
            email=request.POST['email'], password=request.POST['password'])
            request.session['usernametrns'] = member.designation_id
            request.session['usernametrns1'] = member.fullname
            request.session['usernametrns2'] = member.id
            request.session['usernametrns3'] = member.team_id
            return render(request, 'traineesec.html', {'member': member})
        
        
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design3.id).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['m_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['m_id'] = member.id 
            mem=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'MAN_profiledash.html',{'mem':mem,'num':Num,'Num1':Num1,'trcount':trcount})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Adm1.id).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Adm_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['Adm_id'] = member.id 
            Adm=user_registration.objects.filter(id= member.id)
            Num = user_registration.objects.count()
            Num1 = project.objects.count()
            Trainer = designation.objects.get(designation='trainer')
            trcount=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'BRadmin_profiledash.html',{'num':Num,'Num1':Num1,'Adm':Adm,'trcount':trcount})
        
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation_id=design.id).exists():
           
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['usernamets'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['usernametsid'] = member.id
            if request.session.has_key('usernamets'):
                usernamets = request.session['usernamets']
            if request.session.has_key('usernamets1'):
                usernamets1 = request.session['usernamets1']
            else:
                usernamets1 = "dummy"
            mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
            return render(request,'TSdashboard.html',{'mem':mem})
 
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design4.id).exists():
             member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
             request.session['tlid'] = member.id
             if request.session.has_key('tlid'):
                 tlid = request.session['tlid']
             else:
                 variable = "dummy"
             mem = user_registration.objects.filter(id=tlid)
             return render(request, 'TLdashboard.html', {'mem':mem})
            
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design2.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['prid'] = member.id
           
            if request.session.has_key('prid'):
                prid = request.session['prid']
            else:
                variable = "dummy"
            pro = user_registration.objects.filter(id=prid)
            return render(request, 'pmanager_dash.html', {'pro':pro})
        
        
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=design1.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['devid'] = member.id
           
            if request.session.has_key('devid'):
                devid = request.session['devid']
            else:
                variable = "dummy"
            dev = user_registration.objects.filter(id=devid)
            return render(request, 'devdashboard.html', {'dev':dev})

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        if user is not None:
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                request.session['SAdm_id'] = user.id
                Num1 = project.objects.count()
                Num = user_registration.objects.count()
                Trainer = designation.objects.get(designation='trainer')
                trcount=user_registration.objects.filter(designation=Trainer).count()
                return redirect( 'SuperAdmin_dashboard')
            else:
                msg_error = "Password is incorrect"
                return render(request, 'login.html', {'msg_error': msg_error})



        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
        
    return render(request,'login.html')

#######################################################   training Manager   ##############################################
def Dashboard(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametm2)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'Dashboard.html', {'mem': mem ,'labels': labels,'data': data,})
    else:
        return redirect('/')
def Newtrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        des = designation.objects.all()
        dept = department.objects.all()
        team = create_team.objects.all()
        mem1 = designation.objects.get(designation="trainee")
        memm = user_registration.objects.filter(designation_id=mem1).order_by('-id')
        return render(request, 'Newtrainees.html', {'mem': mem, 'memm': memm, 'des': des, 'dept': dept, 'team': team})
    else:
        return redirect('/')

def newtraineeesteam(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        tid = request.GET.get('tid')
        register = user_registration()
        des = designation.objects.all()
        dept = department.objects.all()
        team = create_team.objects.all()
        mem1 = designation.objects.get(designation="trainee")
        memm = user_registration.objects.filter(designation_id=mem1)
        print(memm)
        if request.method == 'POST':
            register = user_registration.objects.get(id=tid)
            
            register.team =create_team.objects.get(id=int(request.POST['team']))
            register.department =department.objects.get(id=int(request.POST['dept']))
            register.designation =designation.objects.get(id=int(request.POST['des']))
            register.save()
            return redirect('Dashboard')
        return render(request, 'Newtrainees.html', {'memm': memm, 'des': des, 'dept': dept, 'team': team, })
    else:
        return redirect('/')

def new_team(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        var = create_team.objects.all().order_by('-id')
        des = designation.objects.get(designation='trainer')
        var1 = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'new_team.html', {'mem': mem, 'var': var, 'var1': var1})
    else:
        return redirect('/')
def new_team1(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        var = user_registration.objects.filter(designation_id=des.id)
        return render(request, 'new_team1.html', {'mem': mem, 'var': var})
    else:
        return redirect('/')
def newteamcreate(request):
    
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        usernametm1 = "dummy"
    if request.method == 'POST':
        team = request.POST['team']
        trainer = request.POST.get('trainer')
        try:
            user= create_team.objects.get(name=team)
            mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
            context = {'msg': 'Team already exists!!!....  Try another name','mem':mem}
            return render(request, 'new_team1.html',context)
        except :
            user= create_team(name=team, trainer=trainer, progress=0)
            user.save()
    return redirect('new_team')
    
def teamdelete(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        usernametm1 = "dummy"

    tid = request.GET.get('tid')
    var = create_team.objects.filter(id=tid)
    
    var.delete()
    return redirect("new_team")

def submit(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        usernametm1 = "dummy"
    tid = request.GET.get('tid')
    if request.method == 'POST':
        var1 = create_team.objects.get(id=tid)
        var1.team_status = 1
        print(var1)
        var1.save()
    return redirect("new_team")

def teamupdate(request):
    if request.session.has_key('usernametm'):
        usernametm = request.session['usernametm']
    if request.session.has_key('usernametm1'):
        usernametm1 = request.session['usernametm1']
    else:
        usernametm1 = "dummy"
    if request.method == 'POST':
        tid = request.GET.get('tid')
        abc = create_team.objects.get(id=tid)
        abc.name = request.POST.get('teams')
        abc.trainer = request.POST.get('trainer')
        abc.save()
        return redirect('new_team')
    else:
        pass

def attendance_tm(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
    
        return render(request, 'attendance_tm.html',{'mem':mem})
    else:
        return redirect('/')
def Trainees_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id)
        
        return render(request, 'Trainees_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')

def Trainees_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)   
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
        return render(request, 'Trainees_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
def Trainers_Calendar(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id)
        return render(request,'Trainers_Calendar.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def Trainers_Attendancetable(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainer']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user).order_by('-id')  
    
        return render(request, 'Trainers_Attendancetable.html',{'mem':mem,'vars':attend})
    else:
        return redirect('/')
def Trainee(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        tre = user_registration.objects.filter(designation=des.id).all().order_by('-id')
    
        return render(request, 'traineetable.html', {'tre': tre, 'vars': vars,'mem':mem})
    else:
        return redirect('/')
def reportedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportedissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportissuetrainers(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'reportissuetrainers.html', {'mem': mem})
    else:
        return redirect('/')
def trainerunsolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
       
        cut = reported_issue.objects.filter(reported_to_id=usernametm2,designation_id=des.id,issuestatus=0)
        a=cut.count()
        
        context = {'cut': cut, 'vars': vars, 'mem': mem,'a':a}
        return render(request,'trainerunsolvedissue.html',context)
    else:
        return redirect('/')
def savetmreplaytrnr(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            
            print(vars.reply)
            vars.reply = request.POST['review']
            
            vars.issuestatus = 1
           
            
            vars.save()
        return redirect('reportissuetrainers')
    else:
        return redirect('/')
def trainersolvedissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainersolvedissue.html',context)
    else:
        return redirect('/')
def reportissuetrainees(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request,'reportissuetrainees.html', {'mem': mem})
    else:
        return redirect('/')
def traineesunsolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        # print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=0)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineesunsolved.html', context)
    else:
        return redirect('/')

def savetmreplytrns(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = reported_issue.objects.get(id=id)
            print(vars.reply)
            vars.reply = request.POST['reply']
            
            vars.issuestatus = 1
           
            vars.save()
        return redirect('reportissuetrainees')
    else:
        return redirect('/')
def traineessolved(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainee')
        print(des.id)
        cut = reported_issue.objects.filter(reported_to_id=usernametm2).filter(
            designation_id=des.id).filter(issuestatus=1)
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'traineessolved.html', context)
    else:
        return redirect('/')
def reportissue(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        # cut = user_registration.objects.get(designation_id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        # ree1 = user_registration.objects.get(designation_id=usernametm)
    
        if request.method == 'POST':
          
            vars = reported_issue()
            # print(vars.reply)
            vars.issue = request.POST['issue']
            
            vars.issuestatus = 0
            vars.reporter_id = usernametm2
            vars.designation_id = des1.id
            vars.reported_to = ree
            vars.reported_date = datetime.now()
            vars.save()
            return redirect('reportedissue')
    
        return render(request, 'reportissue.html', {'mem': mem})
    else:
        return redirect('/')
def reportedissuesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
     
        cut = reported_issue.objects.filter(reporter=usernametm2).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'reportedissuesub.html', context)

    else:
        return redirect('/')
def Applyleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'Applyleave.html', {'mem': mem})
    else:
        return redirect('/')
def trainers_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainers_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        return render(request, 'trainees_leave.html', {'mem': mem})
    else:
        return redirect('/')
def trainees_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        return render(request, 'trainees_leavestatus.html', {'mem': mem,'n':n})
    else:
        return redirect('/')
def trainer_leavestatus(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        des = designation.objects.get(designation='trainer')
        n = leave.objects.filter(designation_id=des.id).order_by('-id')
        
    
        return render(request, 'trainer_leavestatus.html', {'mem': mem ,'n': n})
    else:
        return redirect('/')
def Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            print(vars.leave_rejected_reason)
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainers_leave')
    else:
        return redirect('/')
def Trainee_Leave_rejected(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        id = request.GET.get('id')
        if request.method == 'POST':
            vars = leave.objects.get(id=id)       
            
            vars.leave_rejected_reason = request.POST['review']
            print(vars.leave_rejected_reason)
            vars.leaveapprovedstatus = 2
           
            
            vars.save()
        return redirect('trainees_leave')
    else:
        return redirect('/')

def applyleavesub(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='manager')
        des1 = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(id=usernametm2)
        ree = user_registration.objects.get(designation_id=des.id)
        ree1 = user_registration.objects.get(designation_id=usernametm)
        if request.method == 'POST':
            vars = leave()
            vars.from_date = request.POST['from']
            vars.to_date = request.POST['to']
            vars.reason = request.POST['reason']
            vars.leave_status = request.POST['haful']
            vars.leaveapprovedstatus = 0
            vars.user = cut
            vars.designation_id = des1.id
     
            vars.save()
            return redirect('Applyleave')
    
    
        return render(request,'applyleavesub.html', {'mem': mem})
    else:
        return redirect('/')

def Requestedleave(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainingmanager')
        print(des.id)
        cut = leave.objects.filter(designation_id=des.id).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'Requestedleave.html', context)

    else:
        return redirect('/')
def trainers_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
        
    
        mem = user_registration.objects.filter(designation_id=usernametm) .filter(fullname=usernametm1)
        des = designation.objects.get(designation='trainer')
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        
        
        
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainers_leavelist.html', context)
    else:
        return redirect('/')

       
def approvedstatus(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainers_leave')

def approvedstatus_trainee(request,id):
    a=leave.objects.get(id=id)
    a.leaveapprovedstatus=1
    a.save()
    return redirect('trainees_leave')



def trainees_leavelist(request):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        # .objects.filter(reported_to_id=usernametm2)
        des = designation.objects.get(designation='trainee')
       
        cut = leave.objects.filter(designation_id=des.id).filter(leaveapprovedstatus=0).order_by('-id')
        context = {'cut': cut, 'vars': vars, 'mem': mem}
        return render(request,'trainees_leavelist.html', context)

    else:
        return redirect('/')
def trainer(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(
            id=usernametm2)
        des = designation.objects.get(designation='trainer')
        vars = user_registration.objects.filter(designation=des.id).all().order_by('-id')
        context = {'vars': vars, 'mem': mem}
        return render(request,'trainer.html', context)
    else:
        return redirect('/')

def team1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        return render(request, 'Trainer_Team_manager.html', {'d': d, 'mem': mem})

    return redirect('/')
def current(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer=d.fullname).filter(team_status=0).order_by('-id')
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Current_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def task(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        return render(request,'Trainer_Current_task.html',{'d': d, 'mem': mem})
    else:
        return redirect('/')

def Trainer_Current_Assigned(request, id):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
      
    
        mem = user_registration.objects.filter(id=usernametm2)
        d = create_team.objects.get(id=id)
        vars = topic.objects.filter(team_id=d.id).order_by('-id')
        return render(request, 'Trainer_Current_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Currenttrainee(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(team=d.id,designation=des.id).order_by('-id')
        # .filter(designation=des.id)
        # for item in vars:
        #     import pdb;pdb.set_trace()
        #     item['avg']=(item['attitude']+item['creativity']+item['workperformance'])/100
    
    
        return render(request, 'Trainer_Currenttrainees.html', {'vars': vars, 'mem': mem})
    else:
        return redirect('/')

def Empdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        labels = []
        
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        return render(request, 'Trainer_Current_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem ,'labels': labels,'data': data})
    else:
        return redirect('/')

def Trainer_Previousattendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previousattendance.html', {'vars':vars,'mem': mem})
    else:
        return redirect('/')
def List(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
            
        return render(request,'Trainer_Current_AttendanceList.html',{'mem':mem,'vars': vars, 'atten':atten})

    else:
        return redirect('/')
def task1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user_id=d.id).order_by('-id')
    
        return render(request, 'Trainer_Current_task1.html', {'tsk': tsk, 'mem': mem})

    else:
        return redirect('/')
def tdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.get(id=d.id)
        return render(request, 'Trainer_Current_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Previous(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tm = create_team.objects.filter(trainer=d.fullname).filter(team_status=1)
        des = designation.objects.get(designation='trainer')
        cut = user_registration.objects.filter(designation_id=des.id)
        vars = user_registration.objects.filter(
            designation_id=usernametm).filter(fullname=usernametm1)
        return render(request, 'Trainer_Previous_Team.html', {'vars': vars, 'des': des, 'tm': tm, 'cut': cut, 'mem': mem})
    else:
        return redirect('/')

def Previous_Task(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        return render(request, 'Trainer_Previous_Task.html', {'d': d, 'mem': mem})

    return redirect('/')
def Previous_Assigned(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        vars = trainer_task.objects. filter(id=d.id)
        return render(request, 'Trainer_Previous_Assigned.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def Trainer_Previous_Trainees(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(
            team=d.id).filter(designation=des.id).order_by('-id')
        return render(request, 'Trainer_Previous_Trainees_manager.html', {'vars': vars, 'mem': mem})

    else:
        return redirect('/')
def PEmpdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=vars.team.id)
        labels = []
        
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        return render(request, 'Trainer_Previous_Empdetails.html', {'vars': vars, 'tre': tre, 'mem': mem ,'labels': labels,'data': data})
    else:
        return redirect('/')

def PAttendance(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        vars = user_registration.objects.get(id=id)
    
        return render(request, 'Trainer_Previous_Attendance.html',{'mem':mem, 'vars':vars})
    else:
        return redirect('/')
def PList(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'Trainer_Previous_Attendance_List.html',{'mem':mem,'vars': vars, 'atten':atten})
    else:
        return redirect('/')
def Ptask1(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        d = user_registration.objects.get(id=id)
        tsk = trainer_task.objects.filter(user=d.id)
        return render(request, 'Trainer_Previous_Task1.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')

def Ptdetails(request, id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        tsk = trainer_task.objects.get(id=id)
        return render(request, 'Trainer_Previous_Taskdetails.html', {'tsk': tsk, 'mem': mem})
    else:
        return redirect('/')
def traineedetails(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
        
        vars= user_registration.objects.get(id=id) 
        tre = create_team.objects.get(id=vars.team.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=vars.id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]  
        return render(request,'traineedetails.html',{'mem':mem,'vars':vars,'tre':tre ,'labels': labels,'data': data})
    else:
        return redirect('/')
def statusTable(request,id):
    if 'usernametm2' in request.session:
        if request.session.has_key('usernametm'):
            usernametm = request.session['usernametm']
        if request.session.has_key('usernametm1'):
            usernametm1 = request.session['usernametm1']
        else:
            usernametm1 = "dummy"
    
        mem = user_registration.objects.filter(
            designation_id=usernametm) .filter(fullname=usernametm1)
    
        vars= user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=vars
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user)
        
        return render(request,'trainee_statustable.html',{'mem':mem,'vars':vars, 'atten':atten})
    else:
        return redirect('/')
########################################################   trainers      ###############################################


def trainer_dashboard(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrnr2)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'trainer_dashboard.html', {'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')


def trainer_applyleave(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2) 
        return render(request, 'trainer_applyleave.html', {'z': z})
    else:
        return redirect('/')

def trainer_applyleave_form(request):
    if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    z = user_registration.objects.filter(id=usernametrnr2)
    le = user_registration.objects.get(id=usernametrnr2)
    des1 = designation.objects.get(designation='trainer')
    
    if request.method == 'POST':
        mem = leave()
        mem.from_date = request.POST['from']
        mem.to_date = request.POST['to']
        mem.leave_status = request.POST['haful']
        mem.reason = request.POST['reason']
        mem.user = le
        mem.designation_id = des1.id
        mem.leaveapprovedstatus=0       
        mem.save()
        return render(request, 'trainer_applyleave.html', {'z': z})
    return render(request, 'trainer_applyleave_form.html', {'z': z})
    

def trainer_traineesleave_table(request):
    if 'usernametrnr2' in request.session:
        
            
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
    
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainee')
        tm = leave.objects.filter(designation_id=des.id) .all().order_by('-id')
        return render(request, 'trainer_traineesleave_table.html', {'tm': tm, 'z': z})
    else:
        return redirect('/')

def trainer_reportissue(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_reportissue.html', {'z': z})
    else:
        return redirect('/')

# def trainer_reportissue_form(request):
#     if request.session.has_key('usernametrnr'):
#         usernametrnr = request.session['usernametrnr']
#     if request.session.has_key('usernametrnr1'):
#         usernametrnr1 = request.session['usernametrnr1']
#     if request.session.has_key('usernametrnr2'):
#         usernametrnr2 = request.session['usernametrnr2']
#     else:
#         usernametrnr1 = "dummy"
#     z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
#         fullname=usernametrnr1) .filter(id=usernametrnr2)

#     mem = reported_issue()
#     des = designation.objects.get(designation='trainingmanager')
#     cut = user_registration.objects.get(designation_id=des.id)
#     mem1 = user_registration.objects.get(id=usernametrnr2)
#     des1 = designation.objects.get(designation='trainer')
#     print(mem1)
#     if request.method == "POST":
#         mem.issue = request.POST['issues']
#         mem.reported_date = datetime.now()
#         mem.reported_to = cut
#         mem.reporter = mem1
#         mem.designation_id = des1.id
#         mem.issuestatus =0
#         mem.save()
#         return render(request, 'trainer_reportissue.html', {'z': z})
#     return render(request, 'trainer_reportissue_form.html', {'mem': mem, 'z': z})
def trainer_reportissue_form(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
    
        mem = reported_issue()
        des = designation.objects.get(designation='trainingmanager')
        cut = user_registration.objects.get(designation_id=des.id)
        mem1 = user_registration.objects.get(id=usernametrnr2)
        des1 = designation.objects.get(designation='trainer')
        print(mem1)
        if request.method == "POST":
            mem.issue = request.POST['issues']
            mem.reported_date = datetime.now()
            mem.reported_to = cut
            mem.reporter = mem1
            mem.designation_id = des1.id
            mem.issuestatus =0
            mem.save()
            return render(request, 'trainer_reportissue.html', {'z': z})
        return render(request, 'trainer_reportissue_form.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_reportedissue_table(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        des = designation.objects.get(designation='trainee')
        print(des)
        cut = reported_issue.objects.filter(reported_to_id=usernametrnr2).filter(
            designation_id=des.id).filter(issuestatus=0).order_by('-id')
    
        return render(request, 'trainer_reportedissue_table.html', {'cut': cut, 'vars': vars,  'z': z})
    else:
        return redirect('/')

def savereplaytnee(request, id):
    if request.method == 'POST':
        vars = reported_issue.objects.get(id=id)
        print(vars.reply)
        vars.reply = request.POST['reply']
        print('hello')
        vars.issuestatus = 1
        vars.save()
    return redirect('trainer_reportedissue_table')


def trainer_myreportissue_table(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        rm = reported_issue.objects.filter(reporter_id=usernametrnr2).order_by('-id')
    
        return render(request, 'trainer_myreportissue_table.html', {'rm': rm, 'z': z})


    else:
        return redirect('/')
def trainer_topic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
    
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_topic.html', {'z': z})
    else:
        return redirect('/')

def trainer_addtopic(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        crt = create_team.objects.all()
        mem = topic()
        if request.method == 'POST':
            # mem = user_registration()
            mem.team_id = request.POST['select']
            mem.topic = request.POST['topic']
            mem.startdate = request.POST['start']
            mem.enddate = request.POST['end']
            mem.topic_status = 0
            mem.save()
            return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
        return render(request, 'trainer_addtopic.html', {'mem': mem, 'crt': crt, 'z': z})
    else:
        return redirect('/')

def trainer_viewtopic(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
      
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = topic.objects.all().order_by('-id')
        return render(request, 'trainer_viewtopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')
def trainer_attendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainees.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_attendance_trainer_viewattendance.html',{'z':z})
    else:
        return redirect('/')

def trainer_attendance_trainer_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=usernametrnr2).order_by('-id')
        return render(request, 'trainer_attendance_trainer_viewattendancelist.html',{'z':z,'atten':atten})
    else:
        return redirect('/')



def trainer_team(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_team.html', {'z': z})
    else:
        return redirect('/')

def trainer_currentteam(request):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
    
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        tm = create_team.objects.filter(trainer=usernametrnr1).filter(team_status = 0).order_by('-id')
        return render(request,'trainer_current_team_list.html',{'tm':tm, 'z': z})
    else:
        return redirect('/')



def attenperform(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = create_team.objects.get(id=id)
        abc.progress = request.POST['sele']
        abc.save()
    return redirect('trainer_currentteam')


def trainer_currenttrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(
            designation_id=des.id).filter(team_id=d).order_by('-id')
        return render(request, 'trainer_current_trainees_list.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_currenttraineesdetails(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'tre': tre, 'z': z ,'labels': labels,'data': data,})
    else:
        return redirect('/')


def trainer_currentattentable(request, id):
    if 'usernametrnr2' in request.session:
   
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            std = request.POST['startdate']
            edd = request.POST['enddate']
            user=mem
            atten = attendance.objects.filter(date__gte=std,date__lte=edd,user_id=user).order_by('-id')
        return render(request, 'trainer_current_atten_table.html', {'mem': mem, 'z': z,'atten':atten})

    else:
        return render('/')
def trainer_currentperform(request, id):
    if 'usernametrnr2' in request.session:
   
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        if request.method == 'POST':
            mem.attitude = request.POST['sele1']
            mem.creativity = request.POST['sele2']
            mem.workperformance = request.POST['sele3']
            mem.save()
            return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
        return render(request, 'trainer_current_perform.html', {'mem': mem, 'z': z})
    else:
        return render('/')

def trainer_currentattenadd(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        atten = attendance()
        if request.method == 'POST':
            atten.date = request.POST['date']
            atten.user = mem
            atten.attendance_status = request.POST['pres']
            atten.save()
            return render(request, 'trainer_current_tainees_details.html', {'mem': mem, 'atten': atten, 'z': z})
        return render(request, 'trainer_current_atten_add.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainer_previousteam(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
    
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        tm = create_team.objects.filter(trainer=usernametrnr1).filter(team_status = 1).order_by('-id')
        return render(request,'trainer_previous_team_list.html',{'tm':tm, 'z': z})
    else:
        return redirect('/')

def trainer_previoustrainees(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d)
        return render(request, 'trainer_previous_trainess_list.html', {'mem': mem, 'z': z})

    else:
        return redirect('/')
def trainer_previoustraineesdetails(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'): 
            usernametrnr2 = request.session['usernametrnr2']
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        tre = create_team.objects.get(id=mem.team.id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=mem.id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        return render(request, 'trainer_previous_trainees_details.html', {'mem': mem, 'tre': tre, 'z': z ,'labels': labels,'data': data,})
     
    else:
        return redirect('/')
def trainer_previousattentable(request, id):
    if 'usernametrnr2' in request.session:
        
        if  request.session.has_key('usernametrnr2'): 
             usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        mem = user_registration.objects.get(id=id)
        att = attendance.objects.filter(user_id=mem.id).order_by('-id')
        return render(request, 'trainer_previous_atten_table.html', {'mem': mem, 'att': att, 'z': z})
    else:
        return redirect('/')

def trainer_previousperfomtable(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
      
        z = user_registration.objects.filter(id=usernametrnr2)
        num = user_registration.objects.get(id=id)
        return render(request, 'trainer_previous_performtable.html', {'num': num, 'z': z})
    else:
        return redirect('/')

def trainer_current_attendance(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')


def trainer_Task(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_task.html', {'z': z})
    else:
        return redirect('/')

def trainer_teamlistpage(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        tam = create_team.objects.filter(trainer=usernametrnr1,team_status = 0).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
    
        return render(request, 'trainer_teamlist.html', {'tam': tam, 'cut': cut, 'z': z})
    else:
        return redirect('/')

def trainer_taskpage(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        return render(request, 'trainer_taskfor.html', {'d': d, 'z': z})
    else:
        return redirect('/')

def trainer_givetask(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
        des = designation.objects.get(designation='trainee')
        var = user_registration.objects.filter(team_id=d).filter(designation_id=des.id)
        print(var)
    
        
        if request.method == 'POST':
            list= request.POST.get('trainee_list')
            name = request.POST.get('taskname')
            desc = request.POST.get('description')
            files= request.FILES['files']
            start= request.POST.get('start')
            end = request.POST.get('end')
            task_status = 0
            team_name_id = d.id
            
    
            vars = trainer_task(user_id=list,taskname=name,description=desc,files=files,startdate=start,
                    enddate=end,task_status=task_status, team_name_id=team_name_id)
            vars.save()
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var})
        else:
            return render(request, 'trainer_givetask.html', {'z': z, 'var': var})

    else:
        return redirect('/')
def trainer_taskgivenpage(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        d = create_team.objects.get(id=id)
        c = trainer_task.objects.filter(team_name_id=d.id)
        des = designation.objects.get(designation='trainee')
        mem1 = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).order_by('-id')
        mem = user_registration.objects.filter(designation_id=des.id).filter(team_id=d).values_list('id')
        tsk = trainer_task.objects.filter(team_name_id=d.id).filter(user_id__in=mem).order_by('-id')
        
        return render(request, 'trainer_taskgiven.html', {'mem': mem,'mem1': mem1, 'tsk': tsk, 'z': z})
    else:
        return redirect('/')

def trainer_taska(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        return render(request, 'trainer_taska.html', {'z': z})
    else:
        return redirect('/')

def trainer_task_completed_teamlist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(fullname=usernametrnr1).filter(id=usernametrnr2)
    
        tam = create_team.objects.filter(trainer=usernametrnr1,team_status = 1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
        
        return render(request, 'trainer_task_completed_teamlist.html',  {'z': z, 'cut':cut, 'tam':tam})
    else:
        return redirect('/')

def trainer_task_completed_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
        if request.session.has_key('usernametrnr'):
            usernametrnr = request.session['usernametrnr']
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(designation_id=usernametrnr) .filter(
            fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        d = create_team.objects.get(id=id)
    
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
        return render(request, 'trainer_task_completed_team_tasklist.html', {'z': z, 'tsk':tsk})
    else:
        return redirect('/')

def trainer_task_previous_teamlist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
    
        tam = create_team.objects.filter(trainer=usernametrnr1,team_status = 1).order_by('-id')
        des = designation.objects.get(designation='trainee')
        cut = user_registration.objects.filter(designation_id=des.id)
    
        return render(request, 'trainer_task_previous_teamlist.html', {'z': z, 'cut':cut, 'tam':tam})
    else:
        return redirect('/')

def trainer_task_previous_team_tasklist(request, id):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        
        d=create_team.objects.get(id=id)
        tsk = trainer_task.objects.filter(team_name_id=d.id).order_by('-id')
    
        return render(request, 'trainer_task_previous_team_tasklist.html', {'z': z, 'tsk':tsk})

    else:
        return redirect('/')
def trainer_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        return render(request, 'trainer_trainees.html', {'z': z})
    else:
        return redirect('/')

def trainer_current_trainees(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
    
        # import pdb;pdb.set_trace()
        
        z = user_registration.objects.filter(fullname=usernametrnr1,id=usernametrnr2) 
        cut = create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        print(cut)
        des = designation.objects.get(designation='trainee')
        user = user_registration.objects.filter(designation_id=des.id,team_id__in=cut)
        
        return render(request, 'trainer_current_trainees.html', {'z': z, 'n': user})
    else:
        return redirect('/')
################################   NEW    ####################################



def trainer_current_attendance_view(request, id):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        mem = user_registration.objects.get(id=id)
        return render(request, 'trainer_current_attendance_view.html', {'mem': mem, 'z': z})

    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendance(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
        return render(request, 'trainer_attendance_trainees_viewattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')

def trainer_attendance_trainees_viewattendancelist(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user = request.POST['trainee']
            attend=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
        return render(request, 'trainer_attendance_trainees_viewattendancelist.html',{'z':z,'attend':attend})
    else:
        return redirect('/')

def trainer_attendance_trainees_addattendance(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr1'):
            usernametrnr1 = request.session['usernametrnr1']
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        else:
            usernametrnr1 = "dummy"
        z = user_registration.objects.filter(fullname=usernametrnr1) .filter(id=usernametrnr2)
        cut=create_team.objects.filter(trainer=usernametrnr1).values_list('id',flat=True)
        des = designation.objects.get(designation='trainee')
        vars = user_registration.objects.filter(designation=des.id,team_id__in=cut)
       
    
        if request.method == 'POST':
            atten = attendance()
            atten.date = request.POST['date']
            atten.user_id =request.POST['sele']
            atten.attendance_status = request.POST['pres']
    
            atten.save()
        return render(request, 'trainer_attendance_trainees_addattendance.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    
########################################################   trainees       ###############################################
def trainee_dashboard_trainee(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=usernametrns2)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
    
        
        return render(request, 'trainee_dashboard_trainee.html', {'z': z , 'labels': labels,'data': data,})
    else:
        return redirect('/')

def trainee_topic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_topic.html', {'z': z})
    else:
        return redirect('/')

def trainee_currentTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
       
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3) .filter(topic_status=0).order_by('-id')
        return render(request, 'trainee_currentTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def save_trainee_review(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        tid = request.GET.get('tid')
        vars = topic.objects.get(id=tid)
        print(vars.id)
        vars.review = request.POST.get('review')
        vars.topic_status = 1
        print('hello')
        vars.save()
        return redirect('trainee_currentTopic')
    else:
        return redirect('/')

def trainee_previousTopic(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        if request.session.has_key('usernametrns3'):
            usernametrns3 = request.session['usernametrns3']
        else:
            usernametrns1 = "dummy"
        z = user_registration.objects.filter(id=usernametrns2)
        mem = topic.objects.filter(team_id=usernametrns3).filter(topic_status=1)
        return render(request, 'trainee_previousTopic.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_task(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request, 'trainee_task.html', {'z': z})
    else:
        return redirect('/')

def trainee_task_list(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(user_id=usernametrns2).filter(task_status=0).order_by('-id')
        return render(request, 'trainee_task_list.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_task_details(request,id):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        tid = request.GET.get('tid')
        mem = trainer_task.objects.get(id=id)
        if request.method == 'POST':
            mem.user_description = request.POST['description']
            mem.user_files = request.FILES['files']
            mem.submitteddate = datetime.now()
            mem.task_status=1
            mem.save()
            return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
        return render(request, 'trainee_task_details.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_completed_taskList(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        mem = trainer_task.objects.filter(user_id=usernametrns2).filter(task_status='1').order_by('-id')
        return render(request, 'trainee_completed_taskList.html', {'mem': mem, 'z': z})
    else:
        return redirect('/')

def trainee_reported_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        n = reported_issue.objects.filter(reporter_id=usernametrns2).order_by('-id')
        return render(request, 'trainee_reported_issue.html', {'n': n, 'z': z})
    else:
        return redirect('/')

def trainee_report_reported(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        
    
        z=user_registration.objects.filter(designation_id=usernametrns).filter(id=usernametrns2)
        var = reported_issue()
        if request.method == 'POST':
         
    
            
            # ree= user_registration.objects.get(designation_id=mem1)
            var.designation_id=usernametrns
            var.reported_to = user_registration.objects.get(id=int(request.POST['reportto']))
            var.issue = request.POST['report']
            var.reporter_id = usernametrns2
            var.reported_date = datetime.now()
            var.issuestatus=0
            var.save()
            
            
        return render(request, 'trainee_report_reported.html', {'z':z})
    else:
        return redirect('/')

def trainee_report_issue(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        desi = designation.objects.get(designation='trainingmanager')
        mem3 = user_registration.objects.filter(designation_id=desi.id)
    
        
    
        team = create_team.objects.all()
        print(team)
        tre = designation.objects.get(designation='trainer')
        use = user_registration.objects.filter(designation_id=tre.id)
        
        print(use)
        
        
        return render(request, 'trainee_report_issue.html', {'list': mem3, 'memteam': use, 'z': z})
    else:
        return redirect('/')

def trainee_applyleave_form(request):
    if 'usernametrns2' in request.session:
        if request.session.has_key('usernametrns'):
            usernametrns = request.session['usernametrns']
        if request.session.has_key('usernametrns1'):
            usernametrns1 = request.session['usernametrns1']
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        else:
            usernametrns1 = "dummy"
        z = user_registration.objects.filter(id=usernametrns2)
        le = user_registration.objects.get(id=usernametrns2)
        if request.method == 'POST':
            mem = leave()
            mem.from_date = request.POST['from']
            mem.to_date = request.POST['to']
            mem.leave_status = request.POST['haful']
            mem.reason = request.POST['reason']
            mem.user = le
            mem.designation_id=usernametrns
            mem.leaveapprovedstatus=0
            mem.save()
            return render(request, 'trainee_applyleave_form.html', {'z': z})
        return render(request, 'trainee_applyleave_form.html', {'z': z})
    else:
        return redirect('/')



def trainer_applyleave_cards(request):
   
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
       
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        return render(request, 'trainer_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')

def trainer_appliedleave(request):
    if 'usernametrnr2' in request.session:
       
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
        
        z = user_registration.objects.filter(id=usernametrnr2)
        des = designation.objects.get(designation='trainer')
        tm = leave.objects.filter(designation_id=des.id) .all().order_by('-id')
        
        return render(request, 'trainer_appliedleave.html',{'tm': tm, 'z': z})
    else:
        return redirect('/')

def logout4(request):
    if 'usernametrns2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
def logout2(request):
    if 'usernametrnr2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def logout3(request):
    if 'usernametm2' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 
 ############ attendence #############

def trainee_applyleave_cards(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
        
        return render(request, 'trainee_applyleave_cards.html',{'z' : z})
    else:
        return redirect('/')
def trainee_appliedleave(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2)
    
        des = designation.objects.get(designation='trainee')
        n = leave.objects.filter(designation_id=des.id) .all().order_by('-id')
        
        return render(request, 'trainee_appliedleave.html',{'z' : z,'n' : n})
    else:
        return redirect('/')

def Attendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendance(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
        return render(request,'trainees_attendance_viewattendance.html',{'z':z})
    else:
        return redirect('/')
def trainees_attendance_viewattendancelist(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
       
        z = user_registration.objects.filter(id=usernametrns2) 
        
        if request.method == 'POST':
            start=request.POST['startdate']
            end=request.POST['enddate']
            user=usernametrns2
            vars=attendance.objects.filter(date__gte=start,date__lte=end,user_id=user)
           
        return render(request,'trainees_attendance_viewattendancelist.html',{'z':z,'vars':vars})
    else:
        return redirect('/')
    ##########################  Account ############################################
def account_tr_mg(request):
    if 'usernametm2' in request.session:
        
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
        
        mem = user_registration.objects.filter(id=usernametm2)
    
    
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')
def imagechange_tr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('account_tr_mg')
    return render(request, 'account_tr_mg.html')

    





def account_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
    
        return render(request, 'account_trainer.html', {'z': z})
    else:
        return redirect('/')
def imagechange(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainer')
    return render(request, 'account_trainer.html' )



def account_trainees(request):
    if 'usernametrns2' in request.session:
        
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
        z = user_registration.objects.filter(id=usernametrns2)
    
    
        return render(request, 'account_trainees.html', {'z': z})
    else:
        return redirect('/')

def imagechange_trainees(request):
    
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filenamees']
        abc.save()
        return redirect('account_trainees')
    return render(request, 'account_trainees.html' )






###################################  change password ################################  

def changepassword_trainer(request):
    if 'usernametrnr2' in request.session:
        
        if request.session.has_key('usernametrnr2'):
            usernametrnr2 = request.session['usernametrnr2']
    
        z = user_registration.objects.filter(id=usernametrnr2)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrnr2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainer_dashboard.html', {'z': z})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_trainer.html', {'z': z})
    
        return render(request, 'changepassword_trainer.html', {'z': z})
    
    else:
        return redirect('/')
        

def changepassword_tr_mg(request):
    if 'usernametm2' in request.session:
       
        if request.session.has_key('usernametm2'):
            usernametm2 = request.session['usernametm2']
       
        mem = user_registration.objects.filter(id=usernametm2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametm2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'Dashboard.html', {'mem': mem})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'changepassword_tr_mg.html', {'mem': mem})
    
        return render(request, 'changepassword_tr_mg.html', {'mem': mem})

    else:
        return redirect('/')

def changepassword_trainees(request):
    if 'usernametrns2' in request.session:
       
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        
    
        z = user_registration.objects.filter(id=usernametrns2)
    
        if request.method == 'POST':
            abc = user_registration.objects.get(id=usernametrns2)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'trainee_dashboard_trainee.html', {'z': z})
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
                
    
            return render(request, 'changepassword_trainees.html', {'z': z})
    
        return render(request, 'changepassword_trainees.html', {'z': z})
    else:
        return redirect('/')

############################################# Amal ###########################################################
def Admlogout(request):
    if 'Adm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/') 

def Mnlogout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


#********************Admin account setting****************************
def BRadmin_accsetting(request):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_accsetting.html', {'Adm': Adm})
    else:
        return redirect('/')

def BRadmin_accsettingimagechange(request,id):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('BRadmin_accsetting')
        return render(request, 'BRadmin_accsetting.html',{'Adm':Adm})
    else:
        return redirect('/')

#********************Manager account setting****************************

def MAN_accsetting(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_accsetting.html', {'mem': mem})
    else:
        return redirect('/')

def MAN_accsettingimagechange(request,id):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('BRadmin_accsetting')
        return render(request, 'MAN_accsetting.html',{'mem':mem})
    else:
        return redirect('/')


#***************Admin change password*****************
def BRadmin_changepwd(request):
    if 'Adm_id' in request.session:
        
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        
        Adm = user_registration.objects.filter(id=Adm_id)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=Adm_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'BRadmin_profiledash.html', {'Adm': Adm})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})
    
        return render(request, 'BRadmin_changepwd.html', {'Adm': Adm})
    
    else:
        return redirect('/')

#***************Manager change password*****************

def MAN_changepwd(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        mem = user_registration.objects.filter(id=m_id)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=m_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'MAN_profiledash.html', {'mem': mem})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request, 'MAN_changepwd.html', {'mem': mem})
    
        return render(request, 'MAN_changepwd.html', {'mem': mem})
    
    else:
        return redirect('/')


#***********************anandu*****************************************
def MAN_index(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_index.html',{'mem':mem})
    else:
        return redirect('/') 

def MAN_profiledash(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Num = user_registration.objects.count()
        Num1 = project.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount=user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=m_id)
        for i in queryset:
                labels=[i.workperformance,i.attitude,i.creativity]
                data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'MAN_profiledash.html',{'labels':labels,'data':data,'Man1':Man2,'mem':mem,'num':Num,'trcount':trcount,'Num1':Num1})   
    else:
        return redirect('/') 
        
def MAN_employees(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Dept = department.objects.all()
        return render(request,'MAN_employees.html',{'mem':mem,'Dept':Dept})
    else:
        return redirect('/')
        
def MAN_python(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        Dept = department.objects.get(id = id)
        deptid=id
        mem = user_registration.objects.filter(id=m_id)
        Desig = designation.objects.all()
        return render(request,'MAN_python.html',{'mem':mem,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_projectman(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did)
        return render(request,'MAN_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def MAN_proname(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Project_man_data = user_registration.objects.get(id = id)
        return render(request,'MAN_proname.html',{'pro_man_data':Project_man_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_proinvolve(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Pro_data = project.objects.filter(projectmanager_id = id)
        return render(request,'MAN_proinvolve.html',{'pro_data':Pro_data,'mem':mem})
    else:
        return redirect('/')
        
def MAN_promanatten(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        id = id
        return render(request, 'MAN_promanatten.html',{'mem':mem,'id':id})
    else:
        return redirect('/')

def MAN_promanattendsort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'MAN_promanattendsort.html',{'mem1':mem1,'mem':mem,'id':id})
    else:
        return redirect('/')     


def BRadmin_index(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_index.html',{'mem':mem})
    else:
        return redirect('/')
    
def BRadmin_profiledash(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Num = user_registration.objects.count()
        Num1 = project.objects.count()
        Trainer = designation.objects.get(designation='Trainer')
        trcount=user_registration.objects.filter(designation=Trainer).count()
        Man1 = designation.objects.get(designation='Manager')
        Man2 = user_registration.objects.filter(designation = Man1)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=Adm_id)
        for i in queryset:
                labels=[i.workperformance,i.attitude,i.creativity]
                data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'BRadmin_profiledash.html',{'labels':labels,'data':data,'Num1':Num1,'Man1':Man2,'Adm':Adm,'num':Num,'trcount':trcount}) 
    else:
        return redirect('/')

def BRadmin_employees(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Dept = department.objects.all()
        return render(request,'BRadmin_employees1.html',{'Adm':Adm,'Dept':Dept})
    else:
        return redirect('/')

def BRadmin_python(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Dept = department.objects.get(id = id)
        deptid=id
        Adm = user_registration.objects.filter(id=Adm_id)
        Desig = designation.objects.all()
        return render(request,'BRadmin_python.html',{'Adm':Adm,'Desig':Desig,'Dept':Dept,'dept_id':deptid})
    else:
        return redirect('/')
        
def BRadmin_projectman(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did)
        return render(request,'BRadmin_projectman.html',{'pro_man_data':Project_man_data,'Adm':Adm,'project_name':project_name,'Project_man':Project_man})
    else:
        return redirect('/')
        
def BRadmin_proname(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Project_man_data = user_registration.objects.get(id = id)
        return render(request,'BRadmin_proname.html',{'pro_man_data':Project_man_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_proinvolve(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Pro_data = project.objects.filter(projectmanager_id = id)
        return render(request,'BRadmin_proinvolve.html',{'pro_data':Pro_data,'Adm':Adm})
    else:
        return redirect('/')
        
def BRadmin_promanatten(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        return render(request, 'BRadmin_promanatten.html',{'Adm':Adm,'id':id})
    else:
        return redirect('/')

def BRadmin_promanattendsort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request, 'BRadmin_promanattendsort.html',{'mem1':mem1,'Adm':Adm,'id':id})
    else:
        return redirect('/') 


#***********************praveen************************
def BRadmin_trainerstable(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data=user_registration.objects.filter(designation=Trainer)
        topics=topic.objects.all()
        return render(request,'BRadmin_trainerstable.html',{'Adm':Adm,'trainers_data':trainers_data,'topics':topics})
    else:
        return redirect('/') 

    
def BRadmin_Training(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        #team=create_team.objects.filter(user_id=id)
        #return render(request,'BRadmin_Training.html',{'team':team})
            #team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'BRadmin_Training.html',{'team':team,'user':user,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_trainingteam1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'BRadmin_trainingteam1.html',{'id':id,'num':num,'num1':num1,'Adm':Adm})
    else:
        return redirect('/') 
    
def BRadmin_traineestable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'BRadmin_traineestable.html',{'trainees_data':trainees_data,'Adm':Adm}) 
    else:
        return redirect('/') 
        
def BRadmin_trainingprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        trainees_data=user_registration.objects.get(id=id)
        #Trainee = designation.objects.get(designation='Trainee')
        #trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
        return render(request,'BRadmin_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'Adm':Adm})
    else:
        return redirect('/') 
        
def BRadmin_completedtasktable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'BRadmin_completedtasktable.html',{'task_data':task,'Adm':Adm})   
    else:
        return redirect('/')
        
def BRadmin_topictable(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        topics=topic.objects.filter(team=id)
        return render(request,'BRadmin_topictable.html',{'topics':topics,'Adm':Adm})
    else:
        return redirect('/')

def MAN_trainerstable(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Trainer = designation.objects.get(designation='Trainer')
        trainers_data=user_registration.objects.filter(designation=Trainer)
        topics=topic.objects.all()
        return render(request,'MAN_trainerstable.html',{'trainers_data':trainers_data,'topics':topics,'mem':mem})
    else:
        return redirect('/')
        
def MAN_Training(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        #team=create_team.objects.filter(user_id=id)
        #return render(request,'BRadmin_Training.html',{'team':team})
            #team=create_team.objects.all()
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'MAN_Training.html',{'team':team,'user':user,'mem':mem})
    else:
        return redirect('/')
        
def MAN_trainingteam1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'MAN_trainingteam1.html',{'id':id,'num':num,'num1':num1,'mem':mem})
    else:
        return redirect('/')
        
def MAN_traineestable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'MAN_traineestable.html',{'trainees_data':trainees_data,'mem':mem}) 
    else:
        return redirect('/')
        
def MAN_trainingprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        trainees_data=user_registration.objects.get(id=id)
        #Trainee = designation.objects.get(designation='Trainee')
        #trainees_data=user_registration.objects.filter(designation=Trainee)
        user=user_registration.objects.get(id=id)
        num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
        return render(request,'MAN_trainingprofile.html',{'trainees_data':trainees_data,'num':num,'mem':mem})
    else:
        return redirect('/')
        
def MAN_completedtasktable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'MAN_completedtasktable.html',{'task_data':task,'mem':mem})
    else:
        return redirect('/')
        
def MAN_topictable(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        topics=topic.objects.filter(team=id)
        return render(request,'MAN_topictable.html',{'topics':topics,'mem':mem})
    else:
        return redirect('/')



#*******************    anwar     ****************************

def BRadmin_View_Trainers(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did)
        return render(request,'BRadmin_View_Trainers.html', {'Adm':Adm,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def BRadmin_View_Trainerprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')

def BRadmin_View_Currenttraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Currenttraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Previoustraineesoftrainer(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'BRadmin_View_Previoustraineesoftrainer.html',{'Adm':Adm,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeprofile.html', {'Adm':Adm,'user_registration':userreg})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'BRadmin_View_Currenttraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')
        
def BRadmin_View_Currenttraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Currenttraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeprofile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeprofile.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineetasks(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'BRadmin_View_Previoustraineetasks.html',{'Adm':Adm,'trainer_task':tasks})
    else:
        return redirect('/')

def BRadmin_View_Previoustraineeattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Previoustraineeattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_View_Trainerattendance(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'BRadmin_View_Trainerattendance.html', {'Adm':Adm,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewTrainerattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Trainerattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewCurrenttraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Currenttraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def BRadmin_ViewPrevioustraineeattendancesort(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'BRadmin_View_Previoustraineeattendanceview.html',{'Adm':Adm,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def admin_page1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.all()
            return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'BRadmin_attendance.html', {'Adm':Adm,'department':dpt,'designation':dsg,'user_registration':userreg})  
    else:
        return redirect('/')

def admin_page3(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        
        return render(request,'BRadmin_attendanceshow.html',{'Adm':Adm,'atten':atten,'empname1':empname1}) 
    else:
        return redirect('/')

def admin_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'BRadmin_designation.html', {'Desig': Desig,'departments':departments})

def admin_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'BRadmin_employee.html',{'user':user,'dept':dept,'desi':desi})

def MAN_View_Trainers(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        projectname=project.objects.all()
        trainer=designation.objects.get(id=id)
        userreg=user_registration.objects.filter(designation=trainer).filter(department=did)
        return render(request,'MAN_View_Trainers.html', {'mem':mem,'user_registration':userreg, 'project':projectname})
    else:
        return redirect('/')

def MAN_View_Trainerprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Currenttraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Previoustraineesoftrainer(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
       
        user=user_registration.objects.filter(id=id)
        trainee=designation.objects.get(designation='Trainee')
        user2=user_registration.objects.filter(designation=trainee)
        return render(request,'MAN_View_Previoustraineesoftrainer.html',{'mem':mem,'user_registration':user,'user_registration2':user2})
    else:
        return redirect('/')
        
def MAN_View_Currenttraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        userreg=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeprofile.html', {'mem':mem,'user_registration':userreg})
    else:
        return redirect('/')

def MAN_View_Currenttraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        # user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=id)
        return render(request,'MAN_View_Currenttraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Currenttraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Currenttraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineeprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeprofile.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Previoustraineetasks(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        user=user_registration.objects.get(id=id)
        tasks=trainer_task.objects.filter(user=user)
        return render(request,'MAN_View_Previoustraineetasks.html',{'mem':mem,'trainer_task':tasks})
    else:
        return redirect('/')

def MAN_View_Previoustraineeattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Previoustraineeattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_View_Trainerattendance(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        return render(request,'MAN_View_Trainerattendance.html', {'mem':mem,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewTrainerattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Trainerattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewCurrenttraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Currenttraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_ViewPrevioustraineeattendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        usr=user_registration.objects.get(id=id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        return render(request,'MAN_View_Previoustraineeattendanceview.html',{'mem':mem,'adata':adata,'user_registration':usr})
    else:
        return redirect('/')

def MAN_dev_attendance(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_dev_attendance.html') 
    else:
        return redirect('/')
       

def man_page1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        if request.method == "POST":
            empname1=request.POST.get('empname')
            atten=attendance.objects.all()
            return render(request,'MAN_attendanceshow.html',{'mem':mem,'atten':atten,'empname1':empname1}) 
        dpt=department.objects.all()
        dsg=designation.objects.all()
        userreg=user_registration.objects.all()
        return render(request,'MAN_attendance.html', {'mem':mem,'department':dpt,'designation':dsg,'user_registration':userreg}) 
    else:
        return redirect('/')

def man_page3(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        # mem = user_registration.objects.filter(id=m_id)
        
        
        return render(request,'MAN_attendanceshow.html') 
    else:
        return redirect('/')
   
def man_desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.all()
    return render(request, 'MAN_designation.html', {'Desig': Desig,'departments':departments})


def man_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(dept)
    print(desi)
    return render(request, 'MAN_employee.html',{'user':user,'dept':dept,'desi':desi})

#************************  anwar end  *********************************************


 # current projects- sharon
def BRadmin_pythons(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'BRadmin_dept.html',{'proj_det':project_details,'department':depart,'Adm':Adm})
    else:
        return redirect('/')
    
# def BRadmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num})

def BRadmin_projects(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'BRadmin_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_list(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'BRadmin_proj_list.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_det(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_det.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mngrs(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs.html',{'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'BRadmin_proj_mangrs1.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs2(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'BRadmin_proj_mangrs2.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id) 
        project_task = project_taskassign.objects.get(user_id=id)
        tester =tester_status.objects.all()
        return render(request,'BRadmin_daily_report.html',{'proj_task':project_task,'test':tester,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_developers(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers.html',{'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'Adm':Adm})
    else:
        return redirect('/')

# completed projects- subeesh
 
def BRadmin_proj_cmpltd_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_cmpltd_proj_det_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mngrs_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_proj_mangrs1_new(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'BRadmin_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_proj_mangrs2_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'BRadmin_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'Adm':Adm})
        
    else:
        return redirect('/')

def BRadmin_developers_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_daily_report_new(request, id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester,'Adm':Adm})
    else:
        return redirect('/')

 # current projects-sharon -manager module
def MAN_pythons(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        return render(request,'MAN_projects.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.all()
        depart =department.objects.all()
        return render(request,'MAN_dept.html',{'proj_det':project_details,'department':depart,'mem':mem})
    else:
        return redirect('/')
    
# def MAN_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'MAN_profiledash.html',{'proj_det':project_details,'num':Num})

def MAN_projects(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'MAN_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_list(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'MAN_proj_list.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_det(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_det.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs.html',{'proj_det':project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'MAN_proj_mangrs1.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_proj_mangrs2(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'MAN_proj_mangrs2.html',{'user_det':user_det,'proj_det':project_details,'mem':mem,'proj1':proj1})
    else:
        return redirect('/')

def MAN_daily_report(request,id): 
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester =tester_status.objects.all()
        return render(request,'MAN_daily_report.html',{'proj_task':project_task,'test':tester,'mem':mem})
    else:
        return redirect('/')

def MAN_developers(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers.html',{'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

# completed projects- subeesh -manager module
  
def MAN_proj_cmpltd_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_cmpltd_proj_det_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mngrs_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        return render(request,'MAN_proj_mngrs_show.html', {'project': project_details,'mem':mem})
    else:
        return redirect('/')

def MAN_proj_mangrs1_new(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'MAN_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_proj_mangrs2_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.designation_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'MAN_proj_mangrs2_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details,'mem':mem})
        
    else:
        return redirect('/')

def MAN_developers_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_details = project.objects.get(id=id)
        project_task = project_taskassign.objects.filter(tl_id = id)
        progress_bar= tester_status.objects.all()
        return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar,'mem':mem})
    else:
        return redirect('/')

def MAN_daily_report_new(request, id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        project_task = project_taskassign.objects.get(user_id=id)
        tester = tester_status.objects.all()
        return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester,'mem':mem})
    else:
        return redirect('/')

############## end ##########


#reported issue- akhil-admin mod

def BRadmin_Reportedissue_department(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.all()
        return render(request, 'BRadmin_Reportedissue_department.html',{'department':departments,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_Reportedissue(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.all()
        return render(request, 'BRadmin_Reportedissue.html',{'Adm':Adm,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow(request,id,did):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did)
        return render(request,'BRadmin_ReportedissueShow.html',{'Adm':Adm,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')

def BRadmin_ReportedissueShow1(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues,'Adm':Adm})
    else:
        return redirect('/')

#reported issue- akhil-man mod

def MAN_Reportedissue_department(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.all()
        return render(request, 'MAN_Reportedissue_department.html',{'department':departments,'mem':mem})
    else:
        return redirect('/')

def MAN_Reportedissue(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        departments=department.objects.get(id=id)
        deptid=id
        designations=designation.objects.all()
        return render(request, 'MAN_Reportedissue.html',{'mem':mem,'department':departments,'designation':designations,'dept_id':deptid})
    else:
        return redirect('/')

def MAN_ReportedissueShow(request,id,did):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.all()
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation=designations).filter(department=did)
        return render(request,'MAN_ReportedissueShow.html',{'mem':mem,'designation':designations,'reported_issue':reported_issues,'user_registration':user})
    else:
        return redirect('/')

def MAN_ReportedissueShow1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues,'mem':mem}) 
    else:
        return redirect('/')

############## end ##########


#task section-nimisha- man mod

def MAN_tasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_tasks.html',{'mem':mem})
    else:
        return redirect('/')

def MAN_givetask(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc1,sc2)
            catry = tasks(tasks=sc4,files=ogo,
                                      startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'MAN_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'mem':mem})
    else:
        return redirect('/')

def MAN_taskdesignation(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)   
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.all()
        print(Desig)
        return render(request, 'MAN_taskdesignation.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_taskemployee(request):   
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        desig_id = request.GET.get('desig_id')
        emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
        print(emp)
        return render(request, 'MAN_taskemployee.html', {'emp': emp,'mem':mem})
    else:
        return redirect('/')
        
def MAN_currenttasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all()
        return render(request,'MAN_currenttask.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

def MAN_previoustasks(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)  
        names =tasks.objects.all()
        return render(request,'MAN_previoustasks.html',{'names': names,'mem':mem})
    else:
        return redirect('/')

#task section-nimisha- admin mod

def BRadmin_tasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_tasks.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_givetask(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['task']
            sc7 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc4)
            catry = tasks(tasks=sc4,files=ogo,description=sc7,
                                      startdate=sc5, enddate=sc6,department_id = sc1,designation_id = sc2,user_id = sc3)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        emp = user_registration.objects.all()
        return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_taskdesignation(request):  
     
    dept_id = request.GET.get('dept_id')
    # Desig = designation.objects.filter(department_id=dept_id)
    Desig = designation.objects.all()
    print(Desig)
    return render(request, 'BRadmin_taskdesignation.html', {'Desig': Desig,'Adm':Adm})
    

def BRadmin_taskemployee(request): 
      
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(department_id=dept_id)
    print(emp)
    return render(request, 'BRadmin_taskemployee.html', {'emp': emp,'Adm':Adm})
  

def BRadmin_currenttasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.all()
        return render(request,'BRadmin_currenttask.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_previoustasks(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)  
        names =tasks.objects.all()
        return render(request,'BRadmin_previoustasks.html',{'names': names,'Adm':Adm})
    else:
        return redirect('/')

############## end ##########

#upcoming projects -safdhar -admin mod


def BRadmin_upcoming(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'BRadmin_upcomingprojects.html',{'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_viewprojectform(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5, enddate=sc6,extension='0')
            catry.save()
        return render(request,'BRadmin_viewprojects.html',{'Adm':Adm,'desig':desig,'dept':dept,'project':proj})
    else:
        return redirect('/')

def BRadmin_acceptedprojects(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(status='Accepted')
        return render(request,'BRadmin_acceptedprojects.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_rejected(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.filter(status='Rejected')
        return render(request,'BRadmin_rejectedprojectes.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_createproject(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)  
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc5,sc6,ogo,sc1)
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all()	
        return render(request,'BRadmin_createproject.html',{'Adm':Adm,'dept':dept,'desig':desig})
    else:
        return redirect('/')
        
def BRadmin_upcomingpro(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        pro =project.objects.all()
        return render(request,'BRadmin_upcomingpro.html',{'Adm':Adm,'projects': pro})
    else:
        return redirect('/')

def BRadmin_seradmintraineedesi1(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(department_id=dept_id)
        print(Desig)
        return render(request, 'BRadmin_dropdown.html', {'Desig': Desig,'Adm':Adm})
    else:
        return redirect('/')

def BRadmin_seradmindesig(request):
	print("safdhar")
	dept_id = request.GET.get('dept_id')
	Desig = designation.objects.filter(department_id=dept_id)
	print(Desig)
	return render(request, 'BRadmin_giveprojectdropdown.html', {'Desig': Desig})
	
def BRadmin_selectproject(request):
    
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    print(desig_id,dept_id)
    proj = project.objects.all()
    print(proj)
    return render(request, 'BRadmin_selectproject.html',{'project':proj})
    
#upcoming projects -safdhar -man mod


def MAN_upcoming(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_upcomingprojects.html',{'mem':mem})
    else:
        return redirect('/')
        
def MAN_viewprojectform(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        dept = department.objects.all()
        desig = designation.objects.all()
        proj = project.objects.all()
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            print(sc1,sc2)
            progress=0
            catry = project_taskassign(project_id=sc3,description=sc4,startdate=sc5,enddate=sc6,extension='0')
            catry.save()
        return render(request,'MAN_viewprojects.html',{'desig':desig,'dept':dept,'project':proj,'mem':mem})
    else:
        return redirect('/')

def MAN_acceptedprojects(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Accepted')
        return render(request,'MAN_acceptedprojects.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_rejected(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        pro = project.objects.filter(status='Rejected')
        return render(request,'MAN_rejectedprojectes.html',{'projects':pro,'mem':mem})
    else:
        return redirect('/')

def MAN_createproject(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            sc1 = request.POST['Department']
            sc2 = request.POST['designation']
            sc3 = request.POST['projectname']
            sc4 = request.POST['discrip']
            sc5 = request.POST['start']
            sc6 = request.POST['end']
            ogo = request.FILES['img[]']
            print(sc5,sc6,ogo,sc1)
            progress=0
            catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                      description=sc4,
                                      startdate=sc5, enddate=sc6, files=ogo,progress=progress)
            catry.save()
        dept = department.objects.all()
        desig = designation.objects.all() 
        return render(request,'MAN_createproject.html',{'desig':desig,'dept':dept,'mem':mem})
    else:
        return redirect('/')

def MAN_upcomingprojectsview(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        pro =project.objects.all()
        return render(request,'MAN_upcomingprojectsview.html',{'projects': pro,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmintraineedesi1(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(department_id=dept_id)
        print('safdhar')
        return render(request, 'MAN_createprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')

def MAN_seradmindesig(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        print("safdhar")
        dept_id = request.GET.get('dept_id')
        Desig = designation.objects.filter(department_id=dept_id)
        print(Desig)
        return render(request, 'MAN_giveprojectdropdown.html', {'Desig': Desig,'mem':mem})
    else:
        return redirect('/')
        
def Manager_selectproject(request):
    
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    # desig_id = request.GET.get('desig_id')
    # print(desig_id,dept_id)
    proj = project.objects.filter(department_id=dept_id)
    print(proj)
    return render(request,'manager_selectproject.html',{'project':proj})
    
    
#*************************meenu**********************
def newdept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        condent = department.objects.all()
        return render(request,'BRadmin_Department.html',{'condent':condent,'Adm':Adm})
    else:
        return redirect('/')

def add_dept(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,"BRadmin_add_dept.html",{'Adm':Adm})
    else:
        return redirect('/')

def add_deptsave(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        else:
            variable="dummy"
        Adm = user_registration.objects.filter(id=Adm_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            logo = request.FILES['logo']
            a=department(department=depart,files=logo)
            a.save()
            m="Successfully department added"
        return render(request,'BRadmin_add_dept.html',{'m':m,'Adm':Adm})
    else:
        return redirect('/')

def delete(request, id):
    m = department.objects.get(id=id)
    m.delete()
    return redirect('newdept')

def man_newdept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        condent = department.objects.all()
        return render(request,'man_Department.html',{'condent':condent,'mem':mem})
    else:
        return redirect('/')


def man_dept(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        return render(request,"man_add_dept.html",{'mem':mem})
    else:
        return redirect('/')

def man_add_deptsave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            depart = request.POST['dept']
            newfile = request.FILES['newfile']
            a=department(department=depart,files=newfile)
            a.save()
            m="Successfully department added"
        return render(request,'man_add_dept.html',{'m':m,'mem':mem})
    else:
        return redirect('/')

def man_delete(request, id):
    
    m = department.objects.get(id=id)
    m.delete()
    return redirect('man_newdept')


############## end ##########


#######################################################christin########################

def logout(request):
    if 'usernametsid' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def ProMANlogout(request):
    if 'prid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def TLlogout(request):
    if 'tlid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def devlogout(request):
    if 'devid' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')



def internshipform(request):
    branch = branch_registration.objects.all()
    return render(request, 'internship.html',{'branch':branch})

def internship_save(request):
    branch = branch_registration.objects.all()
    a = internship()
    if request.method == 'POST':
        try:
            a.fullname = request.POST['name']
            a.collegename = request.POST['college_name']
            a.reg_date = datetime.now()
            a.reg_no = request.POST['reg_no']
            a.course = request.POST['course']
            a.stream = request.POST['stream']
            a.platform = request.POST['platform']
            a.branch_id  =  request.POST['branch']
            a.start_date =  request.POST['start_date']
            a.end_date  =  request.POST['end_date']
            a.mobile  =  request.POST['mobile']

            a.alternative_no  =  request.POST['alternative_no']

            a.email = request.POST['email']
            a.profile_pic  =  request.FILES['profile_pic']
            a.attach_file  =  request.FILES['attach']
            if (a.end_date<a.start_date):
                return render(request,'internshipregister.html',{'a':a})
            else:
                a.save()
                qr = qrcode.make("https://managezone.in/base_app/admin_code?id=" + str(a.id))
                qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
                with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                        djangofile = File(reopen)
                        a.qr = djangofile

                        a.save()
            return redirect('internshipform')
        except:
            message = "Enter all details !!!"
            return render(request, 'internship.html',{'message':message})
    else:
        print("not")
        return render(request, 'internship.html')



def imagechange_pr(request):
  
    if request.method == 'POST':
        id = request.GET.get('id')
        abc = user_registration.objects.get(id=id)
        abc.photo = request.FILES['filename']
        
        abc.save()
        return redirect('pr_mg')
    return render(request, 'pr_mg.html')

def leave1(request):
    return render(request, 'leave.html')

def man_registration_form(request):
    branch = branch_registration.objects.all()
    return render(request, 'man_registration_form.html',{'branch':branch})

def man_registration_formsave(request):
    branch = branch_registration.objects.all()
    a = user_registration()
    b = qualification()
    c = extracurricular()
    if request.method == 'POST':
        a.fullname = request.POST['fname']
        a.fathername = request.POST['fathername']
        a.mothername = request.POST['mothername']
        a.dateofbirth = request.POST['dob']
        a.gender = request.POST['gender']
        a.presentaddress1 = request.POST['address1']
        a.presentaddress2  =  request.POST['address2']
        a.presentaddress3 =  request.POST['address3']
        a.pincode = request.POST['pincode']
        a.district  =  request.POST['district']
        a.state  =  request.POST['state']
        a.country  =  request.POST['country']
        a.permanentaddress1 = request.POST['paddress1']
        a.permanentaddress2  =  request.POST['paddress2']
        a.permanentaddress3  =  request.POST['paddress3']
        a.permanentpincode = request.POST['ppincode']
        a.permanentdistrict  =  request.POST['pdistrict']
        a.permanentstate  =  request.POST['pstate']
        a.permanentcountry =  request.POST['pcountry']
        a.mobile = request.POST['mobile']
        a.alternativeno = request.POST['alternative']
        a.email = request.POST['email']
        
        
        a.branch_id = 1
        a.photo = request.FILES['photo']
        a.idproof = request.FILES['idproof']
        a.save()
        
        
        x = user_registration.objects.get(id=a.id)
       
        
        today = date.today()
        tim = today.strftime("%m%y")
        x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
        passw=x.password
        email_id=x.email
        x.save()

       

        b.user_id = a.id
        b.plustwo = request.POST.get('plustwo')
        b.school = request.POST['school']
        b.schoolaggregate = request.POST['aggregate']
        b.schoolcertificate = request.FILES['cupload']
        b.ugdegree = request.POST['degree']
        b.ugstream = request.POST['stream']
        b.ugpassoutyr = request.POST['passoutyear']
        b.ugaggregrate = request.POST['aggregate1']
        b.backlogs = request.POST['supply']
        b.ugcertificate = request.FILES['cupload1']
        b.pg = request.POST['pg']
        b.save()

        c.user_id = a.id
        c.internshipdetails = request.POST['details']
        c.internshipduration = request.POST['duration']
        c.internshipcertificate = request.POST['certificate']
        c.onlinetrainingdetails = request.POST['details1']
        c.onlinetrainingduration = request.POST['duration1']
        c.onlinetrainingcertificate= request.POST['certificate1']
        c.projecttitle = request.POST['title']
        c.projectduration = request.POST['duration2']
        c.projectdescription = request.POST['description']
        c.projecturl = request.POST['url']
        c.skill1 = request.POST['skill1']
        c.skill2 = request.POST['skill2']
        c.skill3 = request.POST['skill3']
        c.save()
        
        subject = 'Greetings from iNFOX TECHNOLOGIES'
        message = 'Congratulations,\n You have successfully registered with iNFOX TECHNOLOGIES.\n following is your login credentials for taking aptitude test\n username :'+str(email_id)+'\n' 'password :'+str(passw)+'\n'
        email_from = settings.EMAIL_HOST_USER
        
        recipient_list = [email_id, ]
        send_mail(subject,message,email_from,recipient_list,fail_silently=False)
        
        abc = user_registration.objects.get(id=a.id)
        newps = request.POST["password"]
        cmps = request.POST["conpassword"]
        if newps == cmps:
            abc.password = request.POST.get('conpassword')
            abc.save()
        else:
            msg_success = "password missmatch error"
            return render(request, 'man_registration_form.html',{'msg_success':msg_success})
        return render(request, 'man_registration_form.html',{'branch':branch})
    else:

        return render(request, 'man_registration_form.html')


def promanagerindex(request):
    return render(request, 'promanagerindex.html')
    
    
def pr_mg(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            usernametm1 = "dummy"
        mem = user_registration.objects.filter(id=prid)
        return render(request, 'account_tr_mg.html', {'mem': mem})
    else:
        return redirect('/')

def pmanager_dash(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'pmanager_dash.html',{'pro':pro})
    else:
        return redirect('/')

def projectmanager_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_projects.html',{'pro':pro})
    else:
        return redirect('/')

#nirmal
def projectmanager_assignproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
       
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        d = designation.objects.get(designation="team leader")
        d1 = d.id
        spa = user_registration.objects.filter(projectmanager_id=prid).filter(designation_id=d1)
        pvar = project.objects.all()
        
        if request.method =='POST':
            
            var = project_taskassign()
            # print("hii")
            var.user_id = prid
            var.tl_id = request.POST['pname']
            var.task = request.POST['task']
            var.description=request.POST.get('desc')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            var.projectfiles=request.FILES.get('pfile')
            var.project_id = request.POST.get('yyy')

            var.save()
            new = project.objects.get(id=var.project_id)
            new.status = "assigned"
            new.save()

            return render(request, 'projectmanager_assignproject.html',{'pro':pro})
        return render(request, 'projectmanager_assignproject.html', {'pro':pro,'spa':spa,'pvar':pvar})
    else:
        return redirect('/')
   
#jensin
def projectmanager_createproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
      
            
        mem = user_registration.objects.filter(id=prid)  
        if request.method =='POST':
            mem = user_registration.objects.filter(id=prid)
            mem2 = user_registration.objects.get(id=prid)
            var = project()
            var.projectmanager_id = prid
            var.department_id = mem2.department_id
            var.project=request.POST.get('pname')
            var.startdate=request.POST.get('sdate')
            var.enddate=request.POST.get('edate')
            var.description=request.POST.get('desc')
            var.files=request.POST.get('pfile')
            
            var.save()
        return render(request, 'projectmanager_createproject.html',{'pro':mem})
    else:
        return redirect('/')

    # if 'prid' in request.session:
    #     if request.session.has_key('prid'):
    #         prid = request.session['prid']
       
    #     else:
    #         variable = "dummy"
    #     pro = user_registration.objects.filter(id=prid)
    #     if request.method == 'POST':
    #         prj =  project()
    #         prj.projectmanager = prid
    #         prj.department = pro.department
         

    #     return render(request, 'projectmanager_createproject.html',{'pro':pro})
    # else:
    #     return redirect('/')

#maneesh
def projectmanager_description(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(id=id)  
        return render(request, 'projectmanager_description.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_table(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        projects = project.objects.filter(status__isnull = True)
        return render(request, 'projectmanager_table.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


def projectmanager_upprojects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectmanager_upprojects.html',{'pro':pro})
    else:
        return redirect('/')

#praveesh

def projectmanager_accepted_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        projects = project.objects.filter(status="accepted")
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectManager_accepted_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')

def projectmanager_rejected_projects(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        projects = project.objects.filter(status="rejected")
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectManager_rejected_projects.html',{'pro':pro,'projects':projects})
    else:
        return redirect('/')


#bibin #amal #abin #rohit
def manindex(request):
    return render(request, 'manager_index.html')

def projectmanEmp(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_emp.html', {'pro': pro})
    else:
        return redirect('/')

def projectmanDev(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(projectmanager_id = prid).filter(~Q(tl_id="0"))
        return render(request, 'projectman_dev.html',{'pro':pro,'man':man})
    else:
        return redirect('/')

def projectmanDevDashboard(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.get(id=id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=prid)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectman_dev_Dashboard.html',{'labels':labels,'data':data,'pro':pro,'man':man})
    else:
        return redirect('/')


def projectman_developer_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectman_team_attendance.html',{'pro':pro})
    else:
        return redirect('/')

def projectman_team(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid) 
        teamid = user_registration.objects.filter(tl_id=id) 
        return render(request, 'projectman_team.html',{'pro': pro,'teamid': teamid})
    else:
        return redirect('/')  

def projectman_team_profile(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)  
        ind = user_registration.objects.filter(id=id) 
        return render(request, 'projectman_team_profile.html',{'pro': pro,'ind': ind})
    else:
        return redirect('/')  

def projectman_team_attendance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(id=id)  
        return render(request,'projectman_team_attendance.html',{'pro':pro,'man':man})
    else:
        return redirect('/')  
def projectman_team_attandance(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        man = attendance.objects.filter(user_id=id)  
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=id) 
        return render(request, 'projectman_team_attandance.html', {'pro': pro,'mem1':mem1,'man':man})
    else:
        return redirect('/')
def projectMANattendance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANattendance.html',{'pro':pro})
    else:
        return redirect('/')  
def projectMANattandance(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            prm1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=prid)
        return render(request, 'projectMANattendancesort.html',{'pro':pro,'prm1':prm1})
    else:
        return redirect('/') 



# def projectMANreportsuccess(request):
#     if 'prid' in request.session:
#         if request.session.has_key('prid'):
#             prid = request.session['prid']
#         else:
#             variable="dummy"
#         pro = user_registration.objects.filter(id=prid)
#         if request.method == 'POST':
#             # uid=objects.GET.get('user_id')
#             vars = reported_issue()
#             vars.issue=request.POST.get('report')
#             vars.reported_date=datetime.datetime.now()
#             vars.reported_to_id=2
#             vars.reporter_id=prid
#             vars.status='pending'
#             vars.save()
#         return render(request, 'MANreportsuccess.html',{'pro':pro})
#     else:
#         return redirect('/')  

def projectMANleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANleave.html',{'pro':pro})
    else:
        return redirect('/') 

def projectMANleavereq(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == "POST":
            
            
            mem = leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = request.POST.get('pr_id')
            mem.status = "pending"
            mem.save()
        return render(request, 'projectMANleavereq.html',{'pro':pro})  
    else:
        return redirect('/')




def projectMANreqedleave(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        var = leave.objects.filter(user_id=prid)
        return render(request, 'projectMANreqedleave.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def Manager_employees(request):
    return render(request,'Manager_employees.html')

def projectManager_tl(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        p = designation.objects.get(designation="team leader")
        p1 = p.id
        tlfil = user_registration.objects.filter(projectmanager_id=prid).filter(designation_id=p1)
        return render(request, 'projectManager_tl.html', {'pro': pro, 'tlfil': tlfil})
    else:
        return redirect('/')


def projectManager_tl_dashboard(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        tls = user_registration.objects.filter(id=id) 
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=prid)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'projectManager_tl_dashboard.html',{'labels':labels,'data':data,'pro': pro, 'tls': tls})
    else:
        return redirect('/')



def man_tl_attendance(request):
    return render(request,'man_tl_attendance.html')

def projectmanager_currentproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        var=project.objects.filter(projectmanager_id=prid,status="assigned")
        return render(request, 'projectmanager_currentproject.html',{'pro':pro,'var':var}) 
    else:
        return redirect('/')

def projectmanager_currentdetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        display = project.objects.filter(id=id)
        return render(request, 'projectmanager_currentdetail.html',{'pro':pro,'display':display})
    else:
        return redirect('/')
def projectmanager_currentteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        
        display = project_taskassign.objects.filter(project_id=id,developer_id__isnull=False)
      
        return render(request, 'projectmanager_currentteam.html',{'pro':pro,'display':display})
    else:
        return redirect('/')
def projectmanager_completeteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        display = project_taskassign.objects.filter(project_id=id)
        return render(request, 'projectmanager_completeteam.html',{'pro':pro,'display':display})
    else:
        return redirect('/')


def projectmanager_currenttl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"

        pro = user_registration.objects.filter(id=prid)
        display2 = user_registration.objects.all()
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        
        return render(request, 'projectmanager_currenttl.html',{'pro':pro,'display':display,'display2':display2})
    else:
        return redirect('/')

    
def projectmanager_completeproject(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        asus = project.objects.filter(status="completed")
        return render(request, 'projectmanager_completeproject.html',{'pro':pro,'asus':asus})
    else:
        return redirect('/')

def projectmanager_completedetail(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        val = project.objects.filter(id=id)
        return render(request, 'projectmanager_completedetail.html',{'pro':pro,'val':val})
    else:
        return redirect('/')



def projectmanager_teaminvolved(request, id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        pri = project_taskassign.objects.filter(developer_id=id)
        return render(request, 'projectmanager_teaminvolved.html',{'pro': pro, 'pri': pri})
    else:
        return redirect('/')


def projectmanager_devteam(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        man = user_registration.objects.filter(tl_id = id)
        return render(request, 'projectmanager_devteam.html',{'pro':pro,'man':man})
    else:
        return redirect('/')



def projectmanager_completetl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=prid)
        com = project.objects.filter(status = "completed")
        display = project_taskassign.objects.filter(project_id=id).values('project_id','tl_id').distinct()
        user = user_registration.objects.all()

        return render(request, 'projectmanager_completetl.html',{'pro':pro,'com':com,'display':display,'user':user})
    else:
        return redirect('/')


def projectMANreportedissue(request):
    if 'prid' in request.session:
        if request.session.has_key('devdes'):
            devdes = request.session['devdes']
        if request.session.has_key('devdep'):
            devdep = request.session['devdep']
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        var=reported_issue.objects.filter(reporter=prid)
    
        return render(request, 'projectMANreportedissue.html',{'var':var,'pro':pro})
    else:
        return redirect('/')
def projectMANreportissue(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        return render(request, 'projectMANreportissue.html',{'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue2(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')

def projectmanagerreportedissue3(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        rid=request.GET.get('rid')
        var=reported_issue.objects.filter(id=id)
        
        return render(request, 'projectmanagerreportedissue2.html',{'var':var,'pro':pro})
    else:
        return redirect('/')




def MANreportsuccess(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        pro1 = user_registration.objects.get(id=prid)
        design=designation.objects.get(designation="manager")
        man = user_registration.objects.get(branch_id=pro1.branch_id,designation_id=design.id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=prid
            vars.status='pending'
            vars.save()
        return render(request, 'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


def projectmanager_tlreported(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
    
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        vars=user_registration.objects.filter(designation=1)
        var=reported_issue.objects.filter(reported_to_id=prid)
        # vars=user_registration.objects.filter(designation_id=2).filter(id=devid)
        return render(request, 'projectmanager_tlreported.html',{'var':var,'vars':vars,'pro':pro})
    else:
        return redirect('/')

def projectreply(request,id):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.save()
        return redirect('projectmanager_tlreported')
    else:
        return redirect('/')

def projectreplytl(request,id):
    if 'prid' in request.session:
        if request.session.has_key('tlid'):
            prid = request.session['tlid']
        else:
            variable = "dummy"
        pro = user_registration.objects.filter(id=prid)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('devtlreported')
    else:
        return redirect('/')

def projectMANreportedissues(request):
    if 'prid' in request.session:
        if request.session.has_key('prid'):
            prid = request.session['prid']
        pro = user_registration.objects.filter(id=prid)
        return render(request,'projectMANreportedissues.html',{'pro':pro})
    else:
        return redirect('/')


#-------------------------------------------------------------------------------------------------------------------------------------

#TL module

def TLdashboard(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=tlid)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'TLdashboard.html',{'labels':labels,'data':data,'mem':mem})
    else:
        return redirect('/')
def tldevview(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        rid=request.GET.get('rid')
        mem1=reported_issue.objects.filter(id=id)
        
        return render(request, 'tldevview.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')
def TLprojects(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        display1 = project.objects.all()
        display=project_taskassign.objects.filter(tl_id=tlid).values('project_id').distinct()
        return render(request, 'TLprojects.html',{'display':display,'mem':mem,'display1':display1})
    else:
        return redirect('/')

def tlprojecttasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        request.session['splitid']=id
        mem = user_registration.objects.filter(id=tlid)
        mem1 = test_status.objects.filter(subtask_id=id)
        mem2 = tester_status.objects.filter(tester_id=tlid)
        time=datetime.now()
        taskstatus = test_status.objects.all()
        display = project_taskassign.objects.filter(tl_id=tlid).filter(project_id=id)
        tasks = project_taskassign.objects.filter(project_id=id,tl_id = tlid,developer_id__isnull=True)
        mem3 = user_registration.objects.get(id=tlid)
        display1=mem3.fullname
       
        return render(request, 'TLprojecttasks.html',{'display1':display1,'time':time,'display':display,'mem':mem,'mem1':mem1,'mem2':mem2,'taskstatus':taskstatus,'tasks':tasks})
    else:
        return redirect('/')

def extensionsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.extension = request.POST['days']
        task.extension_reason = request.POST['reason']
        task.extension_date = datetime.now()
        task.extension_status = "submitted"
        task.save()
    
    return redirect('TLprojects')
 
def tlprojectsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.projectstatus = request.POST['prostatus']
        task.save()
    return redirect('TLprojects')

def pdetailsave(request,id):
    if request.method == 'POST':
        task = project_taskassign.objects.get(id=id)
        task.progress= request.POST['progress']
        task.project_status = request.POST.get('status')
        task.save()
    return redirect('TLprojects')

def extensionapprove(request,id):

    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Approved"
    task.save()
    
    return redirect('TLprojects')

def extensionreject(request,id):
  
    task = project_taskassign.objects.get(id=id)
    task.extension_status = "Rejected"
    task.save()
    
    return redirect('TLprojects')
 

def tltaskstatus(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
       
        mem1 = project_taskassign.objects.get(id=id)
        if request.method == 'POST':
            task = test_status()
            task.date = datetime.now()
            task.workdone = request.POST['workdone']
            task.user_id = tlid
            task.subtask_id = mem1.id
            
            task.files = request.FILES['filed']
            task.save()
        return redirect('TLprojects')
    else:
        return redirect('/')
    
def tlsplittask(request,id):
        if 'tlid' in request.session:
            if request.session.has_key('tlid'):
                tlid = request.session['tlid']
            else:
                variable="dummy"
            splitid = request.session['splitid']
            sub1 = project_taskassign.objects.get(id=id)
            test = test_status.objects.all()
            tester = tester_status.objects.all()
            mem = user_registration.objects.filter(id=tlid)
            sub = project_taskassign.objects.filter(project_id=splitid,tl_id=tlid,developer_id__isnull=False) 
            return render(request, 'TLsplittask.html',{'mem':mem,'sub':sub,'sub1':sub1,'test':test,'tester':tester})
        else:
            return redirect('/') 

def tlgivetask(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        splitid = request.session['splitid']
      
        mem = user_registration.objects.filter(id=tlid)
       
        e = designation.objects.get(designation="tester")
        e1 = e.id
        spa = user_registration.objects.filter(tl_id=tlid)
        spa1 = user_registration.objects.filter(designation_id=e1)
        time=datetime.now()
        tasks = project_taskassign.objects.filter(tl_id=tlid,project_id=splitid,developer_id__isnull=True)
        new = project.objects.get(id=splitid)
        if request.method =='POST':
            
            var = project_taskassign()
            # print("hii")
           
            var.developer_id =  request.POST['ename']
            var.tl_id = tlid
            var.tester_id = request.POST['tname']
            var.tl_description=request.POST.get('description')
            var.subtask=request.POST.get('subtask')
            var.task = request.POST.get('task')
            var.startdate= time
            var.enddate= request.POST.get('date')
            var.files=request.FILES['files']
            var.extension=0
            var.project_id = splitid
            var.description = new.description
            var.save()
        return render(request, 'TLgivetask.html',{'mem':mem,'spa':spa,'spa1':spa1,'time':time,'tasks':tasks})
    else:
        return redirect('/')

def TLattendance(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLattendance.html',{'mem':mem})
    else:
        return redirect('/')

def TLattendancesort(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=tlid)
        return render(request, 'TLattendancesort.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')   

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/') 

def TLreportissues(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreportissues.html',{'mem':mem})
    else:
        return redirect('/')   

def TLreportedissue1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reporter_id=tlid)
        return render(request, 'TLreportedissue1.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   

def TLreportedissue2(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(id=id)
        return render(request, 'TLreportedissue2.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
   
def TLreport1(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"    
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLreport1.html',{'mem':mem})
    else:
        return redirect('/')

def devtlreported(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=tlid)
        var=reported_issue.objects.filter(reported_to_id=tlid)
        return render(request, 'devtlreported.html',{'mem':mem,'var':var})
    else:
        return redirect('/')   
 
def TLreportsuccess(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable="dummy"    
        mem = user_registration.objects.filter(id=tlid)
        mem1 = user_registration.objects.get(id=tlid)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=mem1.projectmanager_id
            vars.reporter_id=tlid
            vars.status='pending'
            vars.save()
        return render(request, 'TLreportsuccess.html',{'mem':mem})
    else:
        return redirect('/')


def TLtasks(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        task = project_taskassign.objects.filter(tl_id=tlid,developer_id__isnull = True)
        return render(request, 'TLtasks.html',{'mem':mem,'task':task})
    else:
        return redirect('/')

def TLtaskformsubmit(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            var = datetime.now()
            task = project_taskassign.objects.get(id=id)
            task.employee_description = request.POST['description']
            task.employee_files = request.FILES['scn']
            task.submitted_date = var
            task.status = 'submitted'
            task.save()
        return render(request, 'TLsuccess.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

def TLleavereq(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleavereq.html',{'mem':mem})
    else:
        return redirect('/')


def TLreqedleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        var = leave.objects.filter(user_id=tlid)
        return render(request, 'TLreqedleave.html',{'var': var,'mem':mem})
    else:
        return redirect('/')

def tl_leave_form(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        if request.method == "POST":
            leaves = leave()
            leaves.from_date = request.POST['from']
            leaves.to_date = request.POST['to']
            leaves.leave_status = request.POST['haful']
            leaves.reason = request.POST['reason']
            leaves.user_id = tlid
            leaves.status = "submitted"
            leaves.save()
        return render(request, 'TLleavereq.html',{'mem':mem})   
    else:
        return redirect('/')


def TLgivetasks(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        time = datetime.now()
        task = project_taskassign.objects.filter(tl_id=tlid).filter(id=id)
        return render(request, 'TLgivetasks.html', {'mem': mem, 'task': task, 'time': time})
    else:
        return redirect('/')

def TLgavetask(request,id):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        task = project_taskassign.objects.filter(tl_id=tlid).filter(id=id)
        return render(request, 'TLgavetask.html', {'mem': mem, 'task': task})
    else:
        return redirect('/')

def TLleave(request):
    if 'tlid' in request.session:
        if request.session.has_key('tlid'):
            tlid = request.session['tlid']
        else:
            variable = "dummy"
        mem = user_registration.objects.filter(id=tlid)
        return render(request, 'TLleave.html',{'mem':mem})
    else:
        return redirect('/')


#------------------------------------------------------------------------------------------------------

#tester module

def TSdashboard(request):
    if 'usernametsid' in request.session:
       
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
            usernamets1 = "dummy"
        mem=user_registration.objects.filter(designation_id=usernamets).filter(fullname=usernamets1)
        return render(request,'TSdashboard.html',{'mem':mem})
    else:
        return redirect('/')

def TStask(request):
    if 'usernametsid' in request.session:

        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
            usernamets1 = "dummy"
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        tasks = project_taskassign.objects.filter(developer=usertsid)
        return render(request,'TStask.html',{'mem':mem,'tasks':tasks})
    else:
        return redirect('/')



def TSproject(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
            usernamets1 = "dummy"
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        pros = project_taskassign.objects.filter(tester=usertsid).values('project_id').distinct()
        new = project.objects.all()
 
        return render(request,'TSproject.html',{'mem':mem,'pros':pros,'new':new})
    else:
        return redirect('/')

def TSprojectdetails(request,pid):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        if request.session.has_key('usernametsid'):
            usertsid = request.session['usernametsid']
        else:
            usernamets1 = "dummy"
    

        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        var = project_taskassign.objects.filter(project=pid,tester_id=usertsid)
        data = tester_status.objects.filter(project_id=pid)
        data1 = test_status.objects.filter(project_id=pid)

        date1= datetime.now()
        return render(request,'TSprojectdetails.html',{'date1':date1,'mem':mem,'var':var,'data':data,'data1':data1})
    else:
        return redirect('/')

def testersave(request,uid,pid):

    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
        usernamets1 = "dummy"
    pr = project_taskassign.objects.get(id=pid)
    user = user_registration.objects.get(id=uid)
    if request.method == 'POST':
        test = tester_status()
        test.tester_id = usertsid
        test.project_id = pr.project_id
        test.user_id = user.id
        test.progress = pr.progress
        test.subtask_id = pid
        test.workdone = request.POST.get('workdone')
        test.files = request.FILES['files']
        test.save()
        return redirect(TSproject)



def projectdetailsave(request,uid,pid):
    if request.session.has_key('usernametsid'):
        usertsid = request.session['usernametsid']
    else:
        usernamets1 = "dummy"
    if request.method == 'POST':
        
        user = project_taskassign.objects.get(developer_id=uid,id=pid)
        user.progress = request.POST.get('dprogress')
        user.projectstatus = request.POST.get('sp')
        user.save()
        return redirect(TSproject)


def TSassigned(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
            usernamets1 = "dummy"
        
        data = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSassigned.html',{'mem':mem,'data':data})
    else:
        return redirect('/')

def TSsubmitted(request,id):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
            usernamets1 = "dummy"
        
        var = project_taskassign.objects.get(id=id)
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsubmitted.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def TSsubmittedsave(request,id):
    if 'usernametsid' in request.session:
        if request.method =='POST':
            
            a = project_taskassign.objects.get(id=id)
            a.employee_description = request.POST.get('empdescription')
            a.employee_files = request.FILES.get('empfile')
            a.submitted_date = datetime.now()
            a.status = "submitted"
            a.save()
            return redirect('TStask')
        else:
            pass
    else:
        return redirect('/')


def TSsucess(request):
    if 'usernametsid' in request.session:
        if request.session.has_key('usernamets'):
            usernamets = request.session['usernamets']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
            usernamets1 = "dummy"
        mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
        return render(request,'TSsucess.html',{'mem':mem})
    else:
        return redirect('/')

#-----------------------------------------------------------------------------------------------------------------------------------------

#developer module

def devindex(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devindex.html', {'dev': dev})


def devdashboard(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=devid)
    for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'devdashboard.html', {'labels':labels,'data':data,'dev': dev})


def devReportedissues(request):
    if 'devid' in request.session:    
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
            variable = "dummy"
        dev = user_registration.objects.filter(id=devid)
        return render(request,'devReportedissues.html',{'dev':dev})
    else:
        return redirect('/')


def devreportissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
            variable = "dummy"
        dev = user_registration.objects.filter(id=devid)
        var=reported_issue.objects.filter(reporter_id=devid)    
        return render(request,'devreportissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devreportedissue(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
    
        else:
            variable = "dummy"
        
        var=reported_issue.objects.filter(reporter_id=devid)  
        dev = user_registration.objects.filter(id=devid)  
        return render(request,'devreportedissue.html',{'var':var,'dev':dev})
    else:
        return redirect('/')


def devsuccess(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        
        dev = user_registration.objects.filter(id=devid)
        tl = user_registration.objects.get(id=devid)
        if request.method == 'POST':           
            vars = reported_issue()
            vars.issue=request.POST.get('reportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=tl.tl_id
            vars.reporter_id=devid
            vars.status='pending'
            vars.save()
        return render(request,'devsuccess.html',{'dev':dev})
    else:
        return redirect('/')


def devissues(request,id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    man = reported_issue.objects.filter(id=id)
    return render(request, 'devissues.html', {'dev': dev,'man':man})


def devsample(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'devsample.html', {'dev': dev})


# *********************praveesh*********************


def Devapplyleav(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav.html', {'dev': dev})


def dev_leave_form(request):
    if request.method == "POST":
        leaves = leave()
        leaves.from_date = request.POST['from']
        leaves.to_date = request.POST['to']
        leaves.leave_status = request.POST['haful']
        leaves.reason = request.POST['reason']
        leaves.user_id = request.POST['dev_id']
        leaves.status = "pending"
        leaves.save()
        return render(request, 'Devapplyleav.html')
    else:
        return render(request, 'Devapplyleav1.html')


def Devapplyleav1(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav1.html', {'dev': dev})


def Devapplyleav2(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav2.html', {'dev': dev})


def Devleaverequiest(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    devl = leave.objects.filter(user_id=devid)
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devleaverequiest.html', {'dev': dev, 'devl': devl})

def Devattendance(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
            variable = "dummy"
        dev = user_registration.objects.filter(id=devid)
        return render(request, 'Devattendance.html', {'dev': dev})
    else:
        return redirect('/')

def Devattendancesort(request):
    if 'devid' in request.session:
        if request.session.has_key('devid'):
            devid = request.session['devid']
        else:
            variable = "dummy"
        dev = user_registration.objects.filter(id=devid)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=devid)          
        return render(request, 'Devattendancesort.html',{'dev':dev,'mem1':mem1})
        
    else:
        return redirect('/')


def Tattend(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Tattend.html', {'dev': dev})


def Devapplyleav3(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'Devapplyleav3.html', {'dev': dev})


# **************************maneesh*******************************


def DEVprojects(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    pros = project.objects.all()
    devp = project_taskassign.objects.filter(developer_id=devid).values('project_id').distinct()
    return render(request, 'DEVprojects.html', {'dev': dev, 'devp': devp, 'pros': pros})


def DEVtable(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    devp = project_taskassign.objects.filter(project_id=id).filter(developer_id=devid)
    teststatus = test_status.objects.all()
    testerstatus = tester_status.objects.filter(project_id=id)
    time = datetime.now()
    return render(request, 'DEVtable.html', {'dev': dev, 'devp': devp, 'time': time, 'teststatus': teststatus, 'testerstatus': testerstatus})


def DEVtaskstatus(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        task = test_status()
        task.date = datetime.now()
        task.workdone = request.POST['workdone']
        task.user_id = devid
        task.subtask_id = mem.id
        task.project_id = mem.project_id
        
        task.files = request.FILES['filed']
        task.save()
    return redirect('DEVprojects')

def DEVextension(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    mem = project_taskassign.objects.get(id=id)
    if request.method == 'POST':
        ext = project_taskassign.objects.get(id=id)
        ext.extension = request.POST['dayz']
        ext.extension_reason = request.POST['resn']
        ext.extension_date = datetime.now()
        ext.extension_status = "submitted"
        ext.save()
    return redirect('DEVprojects')

def devprjsave(request,id):
    if request.method == 'POST':
       
        ext = project_taskassign.objects.get(id=id)
        ext.progress = request.POST['devpro']
        ext.projectstatus = request.POST['devstat']
        ext.save()
      
        return redirect('DEVprojects')


def DEVtaskmain(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid)
    return render(request, 'DEVtaskmain.html', {'dev': dev, 'task': task})


def DEVtaskform(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    time = datetime.now()
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    return render(request, 'DEVtaskform.html', {'dev': dev, 'task': task, 'time': time})

def DEVtaskformsubmit(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    if request.method == "POST":
        task = project_taskassign.objects.get(id=id)
        task.employee_description = request.POST['description']
        task.employee_files = request.FILES['scn']
        task.submitted_date = datetime.now()
        task.status = 'submitted'
        task.save()
    return render(request, 'DEVtasksumitted.html', {'dev': dev, 'task': task})

def DEVtask(request, id):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    task = project_taskassign.objects.filter(developer_id=devid).filter(id=id)
    return render(request, 'DEVtask.html', {'dev': dev, 'task': task})


def dev_task_submit(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    if request.method == "POST":
        dpid = request.POST.get('dpid')
        member = project_taskassign.objects.get(id=dpid)
        member.employee_description=request.POST['workdone']
        member.save()
        return redirect('DEVtable')


def DEVsuccess(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVsuccess.html', {'dev': dev})

def DEVtasksumitted(request):
    if request.session.has_key('devid'):
        devid = request.session['devid']
    else:
        variable = "dummy"
    dev = user_registration.objects.filter(id=devid)
    return render(request, 'DEVtasksumitted.html', {'dev': dev})
    
    
    
    
    
    
    
    #**********************internship****************
    
def man_internship_view(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id)
    return render(request,'man_internship_view.html',{'mem':mem})
    
def BRadmin_internship_view(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_internship_view.html',{'Adm':Adm})

def BRadmin_internship(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)

    var1=internship.objects.all() 
    return render(request,'BRadmin_internship.html',{'var1':var1,'Adm':Adm})
    
def man_internship(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id) 
    var1=internship.objects.all()  
    return render(request,'man_internship.html',{'var1':var1,'mem':mem})

def man_internship_date(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id)
    newdata1 = internship.objects.all().values('reg_date').distinct()
    return render(request,'man_internship_date.html',{'mem':mem,'newdata':newdata1})

def BRadmin_internship_date(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request,'BRadmin_internship_date.html',{'Adm':Adm,'newdata':newdata})
    
def BRadmin_internship_dateview(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    reg_date=request.GET.get('date')
    empid=internship.objects.filter(reg_date=reg_date)
    return render(request,'BRadmin_internship_dateview.html',{'Adm':Adm,'data':empid})
    
def man_internship_dateview(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id)
    reg_date1=request.GET.get('date1')
    empid=internship.objects.filter(reg_date=reg_date1)
    return render(request,'man_internship_dateview.html',{'mem':mem,'data':empid})

def BRadmin_internship_update(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    return render(request,'BRadmin_internship_update.html',{'var':var,'Adm':Adm})
    
def render_pdf_view(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    template_path = 'pdf.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


    
def internshipupdatesave(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    var = internship.objects.get(id=id)
    var.fullname = request.POST['fullname']
    var.collegename = request.POST['college']
    var.reg_no = request.POST['regno']
    var.course = request.POST['course']
    var.stream = request.POST['stream']        
    var.platform = request.POST['platform']        
    #var.branch_id  =  request.POST['branch']        
    var.start_date =  request.POST['startdate']        
    var.end_date  =  request.POST['enddate']        
    var.mobile  =  request.POST['mobile']        
    var.alternative_no  =  request.POST['altmob']        
    var.email = request.POST['email']
    var.hrmanager = request.POST['hrmanager']
    var.guide = request.POST['guide']
    var.rating = request.POST['rating']
    var.save()
    return redirect('BRadmin_internship')

def interndelete(request,id):
    man.delete()
    return redirect('BRadmin_internship')

def maninterndelete(request,id):
    man1 = internship.objects.get(id=id)
    man1.delete()
    return redirect('man_internship')


def certificate_intrn(request,id):

    date = datetime.now()   
    mem = internship.objects.get(id=id)
    mems = internship.objects.filter(id=id)
    template_path = 'certificate_intrn.html'
    context = {'mem': mem, 'mems': mems,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
       
def man_internship_dateview(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id) 
    var1=internship.objects.all()  
    return render(request,'man_internship_dateview.html',{'var1':var1,'mem':mem})
       



#*****************************registration********


def man_registration_update(request,id):
    xem = extracurricular.objects.get(user_id=id)
    qem = qualification.objects.get(user_id=id)
    mem = user_registration.objects.get(id=id)
    return render(request,'man_registration_update.html',{'mem':mem,'qem':qem,'xem':xem})

def man_registration(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"    
    mem = user_registration.objects.filter(id=m_id)
    mem1 = user_registration.objects.all()
    return render(request,'man_registration.html',{'mem':mem,'mem1':mem1})
    
def BRadmin_registration(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    else:
        variable="dummy"    
    Adm = user_registration.objects.filter(id=Adm_id)
    mem1 = user_registration.objects.all()
    return render(request,'BRadmin_registration.html',{'Adm':Adm,'mem1':mem1})

def registrationupdatesave(request,id):
    a = user_registration.objects.get(id=id)
    b = qualification.objects.get(user_id=id)
    c = extracurricular.objects.get(user_id=id)
    if request.method == 'POST':
        a.fullname = request.POST['name']
        a.fathername = request.POST['fathersname']
        a.mothername = request.POST['mothersname']
        #a.dateofbirth = request.POST['dob']
        #a.gender = request.POST['gender']
        a.presentaddress1 = request.POST['presentaddress1']
        a.presentaddress2  =  request.POST['presentaddress2']
        a.presentaddress3 =  request.POST['presentaddress3']
        a.pincode = request.POST['pincode']
        a.district  =  request.POST['district']
        a.state  =  request.POST['state']
       # a.country  =  request.POST['country']
        a.permanentaddress1 = request.POST['permanentaddress1']
        a.permanentaddress2  =  request.POST['permanentaddress2']
        a.permanentaddress3  =  request.POST['permanentaddress3']
        a.permanentpincode = request.POST['permanentpincode']
        a.permanentdistrict  =  request.POST['permanentdistrict']
        a.permanentstate  =  request.POST['permanentstate']
        #a.permanentcountry =  request.POST['pcountry']
        a.mobile = request.POST['mobile1']
        a.alternativeno = request.POST['altmobile1']
        a.email = request.POST['email']
        #a.password= request.POST['password']
        #a.branch_id = request.POST['branch']
        #a.photo = request.FILES['photo']
        #a.idproof = request.FILES['idproof']
        a.save()
        x = user_registration.objects.get(id=a.id)
        today = date.today()
        # mon = datetime( today.month)
        # yr = datetime(today.year)
        # tim = str(mon)+''+str(yr)
        today = date.today()
        tim = today.strftime("%m%y")

        #x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
        x.save()

       

        b.user_id = a.id
        #b.plustwo = request.POST.get('school')
        b.school = request.POST['school']
        b.schoolaggregate = request.POST['aggregate']
        #b.schoolcertificate = request.FILES['cupload']
        b.ugdegree = request.POST['degree']
        b.ugstream = request.POST['stream']
        b.ugpassoutyr = request.POST['passoutyear']
        b.ugaggregrate = request.POST['aggregate1']
        #b.backlogs = request.POST['supply']
        #b.ugcertificate = request.FILES['cupload1']
        b.pg = request.POST['pg']
        b.save()

        c.user_id = a.id
        c.internshipdetails = request.POST['details']
        c.internshipduration = request.POST['duration1']
        c.internshipcertificate = request.POST['certification']
        c.onlinetrainingdetails = request.POST['details1']
        c.onlinetrainingduration = request.POST['duration2']
        c.onlinetrainingcertificate= request.POST['certification1']
        c.projecttitle = request.POST['title']
        c.projectduration = request.POST['duration3']
        c.projectdescription = request.POST['description']
        c.projecturl = request.POST['url']
        c.skill1 = request.POST['skill1']
        c.skill2 = request.POST['skill2']
        c.skill3 = request.POST['skill3']
        c.save()
    return redirect('man_registration')

def registrationdelete(request,id):
    man = user_registration.objects.get(id=id)
    man1 = extracurricular.objects.get(user_id=id)
    man2 = qualification.objects.get(user_id=id)
    man2.delete()
    man1.delete()
    man.delete()
    return redirect('man_registration')

#super admin views #
def superadmin_changepwd(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'superadmin_changepwd.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'superadmin_changepwd.html', {'msg_error': msg_error})
        return render(request,'superadmin_changepwd.html',{'users':users})
    
    

def superadmin_index(request):
    if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
    users = User.objects.filter(id=SAdm_id)
    return render(request,'SuperAdmin_index.html',{'users':users})

def superadmin_logout(request):
    request.session.flush()
    return redirect("/")



#**************************Anandhu Super-Admin Dashboard section**************************

def SuperAdmin_index(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     mem = user_registration.objects.filter(id=Adm_id)
    #     return render(request,'SuperAdmin_index.html',{'mem':mem})
    # else:
    #     return redirect('/')
    return render(request, 'SuperAdmin_index.html')


def SuperAdmin_dashboard(request):
    branch = branch_registration.objects.all()
    
    return render(request, 'SuperAdmin_dashboard.html',{'branch_registration':branch})   


def SuperAdmin_profile(request,id):
    branch = branch_registration.objects.get(id = id)
    Num1 = project.objects.filter(branch_id=id).count()
    Num = user_registration.objects.filter(branch_id=id).count()
    Trainer = designation.objects.get(designation='trainer')
    trcount=user_registration.objects.filter(designation=Trainer,branch_id=id).count()
    return render(request, 'SuperAdmin_profile.html',{'br':branch,'Num1':Num1,'Num':Num,'trcount':trcount}) 


def SuperAdmin_trainersdepartment(request,id):
    Dept = department.objects.filter(branch = id)
    return render(request,'SuperAdmin_trainersdepartment.html',{'Dept':Dept})


def SuperAdmin_trainerstable(request,id):
   

    Trainer = designation.objects.get(designation='Trainer')
        
    trainers_data=user_registration.objects.filter(designation=Trainer).filter(department=id)
    topics=topic.objects.all()
    return render(request,'SuperAdmin_trainerstable.html',{'trainers_data':trainers_data,'topics':topics})

def SuperAdmin_trainerteams(request,id):
   
        user=user_registration.objects.filter(id=id)
        team=create_team.objects.all()
        return render(request,'SuperAdmin_trainerteams.html',{'team':team,'user':user}) 

def  SuperAdmin_trainerteam(request,id):
    
        id=id
        Trainee = designation.objects.get(designation='Trainee')
        num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
        num1=topic.objects.filter(team=id).count()
        return render(request,'SuperAdmin_trainerteam.html',{'id':id,'num':num,'num1':num1})

def SuperAdmin_topictable(request,id):
    
    topics=topic.objects.filter(team=id).order_by("-id")
    return render(request,'SuperAdmin_topictable.html',{'topics':topics})
        
def SuperAdmin_traineestable(request,id):
   
        Trainee = designation.objects.get(designation='Trainee')
        trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
        return render(request,'SuperAdmin_traineestable.html',{'trainees_data':trainees_data}) 

        
def SuperAdmin_traineeprofile(request,id):
   
    trainees_data=user_registration.objects.get(id=id)
    user=user_registration.objects.get(id=id)
    num=trainer_task.objects.filter(user=user).filter(task_status='1').count()
    return render(request,'SuperAdmin_traineeprofile.html',{'trainees_data':trainees_data,'num':num})

def SuperAdmin_completedtasktable(request,id):
        user=user_registration.objects.get(id=id)
        task=trainer_task.objects.filter(user=user)
        return render(request,'SuperAdmin_completedtasktable.html',{'task_data':task})   
   

#**************************subeesh akhil sharon  Super-Admin Dashboard-project section**************************


# current projects- sharon
def SuperAdmin_pythons(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.all()
        return render(request,'SuperAdmin_projects.html',{'proj_det':project_details})
    # else:
    #     return redirect('/')

def SuperAdmin_dept(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        
        project_details = project.objects.all()
        depart =department.objects.filter(branch=id)
        
        return render(request,'SuperAdmin_dept.html',{'proj_det':project_details,'department':depart})
    # else:
    #     return redirect('/')

    
# def SuperAdmin_profiledash(request):
#     Num= project.objects.count()
#     project_details = project.objects.all()
#     return render(request,'SuperAdmin_profiledash.html',{'proj_det':project_details,'num':Num})

def SuperAdmin_projects(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        Num= project.objects.filter(status='accepted').filter(department=id).count()
        num= project.objects.filter(status='completed').filter(department=id).count()
        project_details = project.objects.all()
        depart =department.objects.get(id=id)
        id=id
        return render(request,'SuperAdmin_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id})
    # else:
    #     return redirect('/')
 
def SuperAdmin_proj_list(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'SuperAdmin_proj_list.html',{'proj_det':project_details})
    # else:
    #     return redirect('/')

def SuperAdmin_proj_det(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_det.html',{'proj_det':project_details})
    # else:
    #     return redirect('/')

def SuperAdmin_proj_mngrs(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs.html',{'proj_det':project_details})
    # else:
    #     return redirect('/')

# def SuperAdmin_proj_mangrs1(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id) 
#     return render(request,'SuperAdmin_proj_mangrs1.html',{'proj_det':project_details,'mem':mem})
def SuperAdmin_proj_mangrs1(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details})
    # else:
    #     return redirect('/')

def SuperAdmin_proj_mangrs2(request,id):
    # if request.session.has_key('Adm_id'):
    #     Adm_id = request.session['Adm_id']
 
    # mem = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id) 
    proj1=project_details.projectmanager_id
    dept_id=project_details.department_id
    user_det=user_registration.objects.filter(designation_id=proj1)
    
    return render(request,'SuperAdmin_proj_mangrs2.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details})

def SuperAdmin_daily_report(request,id):



    proj_name =  project_taskassign.objects.all()
    tester_name = user_registration.objects.all()
    tester = tester_status.objects.filter(user_id=id)
    return render(request,'SuperAdmin_daily_report.html',{'test':tester, 'tester_name':tester_name, 'proj_name':proj_name})
def SuperAdmin_developers(request,id):
    # proj2=request.session['proj2']
    # project_details = project.objects.get(id=proj2) 
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.filter(project_id = project_details).filter(tl_id=id)
    user_det=user_registration.objects.filter(tl_id=id).order_by("-id")
    progress_bar= tester_status.objects.all()
    
    return render(request,'SuperAdmin_developers.html',{'proj_task':project_task,'proj_det':project_details,'prog_status':progress_bar,'user_det':user_det})
    # else:
    #     return redirect('/')


# completed projects- subeesh
 
def SuperAdmin_proj_cmpltd_new(request, id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details=project.objects.filter(department=id)
        print (project_details.count())
        return render(request,'SuperAdmin_proj_cmpltd_show.html',{'project': project_details})
    # else:
    #     return redirect('/')


def SuperAdmin_cmpltd_proj_det_new(request, id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_cmpltd_proj_det_show.html',{'project': project_details})
    # else:
    #     return redirect('/')
def SuperAdmin_proj_mngrs_new(request, id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id)
        return render(request,'SuperAdmin_proj_mngrs_show.html', {'project': project_details})
    # else:
    #     return redirect('/')

# def SuperAdmin_proj_mangrs1_new(request,id):
#     if request.session.has_key('Adm_id'):
#         Adm_id = request.session['Adm_id']
 
#     mem = user_registration.objects.filter(id=Adm_id)
#     project_details = project.objects.get(id=id)
#     return render(request,'SuperAdmin_proj_mangrs1_show.html', {'project': project_details,'mem':mem})
def SuperAdmin_proj_mangrs1_new(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        project_details = project.objects.get(id=id) 
        proj1=project_details.projectmanager_id
        dept_id=project_details.department_id
        user_det=user_registration.objects.filter(designation_id=proj1)
        return render(request,'SuperAdmin_proj_mangrs1_show.html',{'proj1':proj1,'user_det':user_det,'proj_det':project_details})
        
    # else:
    #     return redirect('/')
def SuperAdmin_proj_mangrs2_new(request, id):
    # if request.session.has_key('Adm_id'):
    #     Adm_id = request.session['Adm_id']
 
    # mem = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'SuperAdmin_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task})

def SuperAdmin_developers_new(request, id):
    # if request.session.has_key('Adm_id'):
    #     Adm_id = request.session['Adm_id']
 
    # mem = user_registration.objects.filter(id=Adm_id)
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    progress_bar= tester_status.objects.all()
    return render(request,'SuperAdmin_developers_show.html', {'project':project_details,'project_taskassign':project_task,'prog_status':progress_bar})

def SuperAdmin_daily_report_new(request, id):
    # if request.session.has_key('Adm_id'):
    #     Adm_id = request.session['Adm_id']
 
    # mem = user_registration.objects.filter(id=Adm_id)
    project_task = project_taskassign.objects.get(user_id=id)
    tester = tester_status.objects.all()
    return render(request,'SuperAdmin_daily_report_show.html', {'project':project_task,'tester_status':tester})



    #**************************meenu nimisha  Super-Admin Dashboard-employee section**************************

def SuperAdmin_employees(request,id):
    Dept = department.objects.filter(branch=id)
    return render(request,'SuperAdmin_Employees1.html',{'Dept':Dept})

        
def SuperAdmin_edepartments(request,id):
    Dept = department.objects.get(id = id)
    deptid=id        
    Desig = designation.objects.all()
    return render(request,'SuperAdmin_edpartments.html',{'Desig':Desig,'Dept':Dept,'dept_id':deptid})

def SuperAdmin_projectman(request,id,did):
        Project_man= designation.objects.get(id = id)
        project_name = project.objects.filter(designation=Project_man).filter(department=did)
        Project_man_data=user_registration.objects.filter(designation=Project_man).filter(department=did).order_by("-id")
        return render(request,'SuperAdmin_projectman.html',{'pro_man_data':Project_man_data,'project_name':project_name,'Project_man':Project_man})
    

def SuperAdmin_ViewTrainers(request,id,did):       
    projectname=project.objects.all()
    trainer=designation.objects.get(id=id)
    userreg=user_registration.objects.filter(designation=trainer).filter(department=did).order_by("-id")
    return render(request,'SuperAdmin_ViewTrainers.html', {'user_registration':userreg, 'project':projectname})
    


def SuperAdmin_View_Trainerprofile(request,id):  
    userreg=user_registration.objects.get(id=id)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request,'SuperAdmin_View_Trainerprofile.html', {'user_registration':userreg,'labels':labels,'data':data})



def SuperAdmin_View_Currenttraineesoftrainer(request,id):
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='trainee')
    user2=user_registration.objects.filter(designation=trainee)
    return render(request,'SuperAdmin_View_Currenttraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})
   
def SuperAdmin_View_Currenttraineeprofile(request,id):
    userreg=user_registration.objects.get(id=id)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request,'SuperAdmin_View_Currenttraineeprofile.html', {'user_registration':userreg,'labels':labels,'data':data})
   
       
def SuperAdmin_View_Currenttraineetasks(request,id):
        # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'SuperAdmin_View_Currenttraineetasks.html',{'trainer_task':tasks})
    
       
def SuperAdmin_View_Currenttraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Currenttraineeattendance.html', {'user_registration':usr})


def SuperAdmin_ViewCurrenttraineeattendancesort(request,id): 
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_View_Currenttraineeattendancesort.html',{'adata':adata,'user_registration':usr})
    
        
def SuperAdmin_View_Previoustraineesoftrainer(request,id): 
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='trainee')
    user2=user_registration.objects.filter(designation=trainee)
    return render(request,'SuperAdmin_View_Previoustraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def SuperAdmin_View_Previoustraineetasks(request,id):   
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)        
    return render(request,'SuperAdmin_View_Previoustraineetasks.html',{'trainer_task':tasks})


def SuperAdmin_View_Previoustraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Previoustraineeattendance.html', {'user_registration':usr})


def SuperAdmin_ViewPrevioustraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_ViewPrevioustraineeattendancesort.html',{'adata':adata,'user_registration':usr})
    
   
def SuperAdmin_View_Trainerattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'SuperAdmin_View_Trainerattendance.html', {'user_registration':usr})
    


def SuperAdmin_ViewTrainerattendancesort(request,id):  
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request,'SuperAdmin_ViewTrainerattendancesort.html',{'adata':adata,'user_registration':usr})
    

def SuperAdmin_View_Previoustraineeprofile(request,id):   
    usr=user_registration.objects.get(id=id)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request,'SuperAdmin_View_Previoustraineeprofile.html', {'user_registration':usr,'labels':labels,'data':data})
    
    
def SuperAdmin_proname(request,id):
    Project_man_data = user_registration.objects.get(id = id)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request,'SuperAdmin_proname.html',{'pro_man_data':Project_man_data,'labels':labels,'data':data})
    

def SuperAdmin_proinvolve(request,id):
    Pro_data = project.objects.filter(projectmanager_id = id).order_by("-id")
    return render(request,'SuperAdmin_proinvolve.html',{'pro_data':Pro_data})
    
def SuperAdmin_promanatten(request,id):
    id = id
    return render(request, 'SuperAdmin_promanatten.html',{'id':id})
    

def SuperAdmin_promanattendsort(request,id):
    id = id
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
        mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
    return render(request, 'SuperAdmin_promanattensort.html',{'mem1':mem1,'id':id})
    






def SuperAdmin_admin_registration(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        return render(request,'SuperAdmin_admin_registration.html')

def SuperAdmin_registration(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        branches=branch_registration.objects.all()
        
        return render(request,'SuperAdmin_registration.html',{'branches':branches,})

def SuperAdmin_Add(request):
    des=designation.objects.get(designation="admin")
    if request.method == 'POST':
        fn1 = request.POST['fname']
        fn2 = request.POST['faname']
        fn3 = request.POST['adob']
        fn4 = request.POST['agender']
        fn5 = request.POST['amobile']
        fn6 = request.POST['aemail']
        fn7 = request.POST['aalternative']
        fn8 = request.POST['Adminbranch']
        fn9 = request.FILES['aproof']
        fn10 = request.FILES['cphoto']
        
       
        
        new2 = user_registration(fullname=fn1, fathername=fn2, dateofbirth=fn3, gender=fn4, mobile=fn5, email=fn6, alternativeno=fn7,branch_id=fn8,
                                idproof=fn9, photo=fn10,designation_id=des.id)
        new2.save()
        return redirect('SuperAdmin_registration')
    else:
        return redirect('SuperAdmin_registration')




def SuperAdmin_admin_view(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
    designations=designation.objects.get(designation='Admin')
    user=user_registration.objects.filter(designation=designations)
    return render(request,'SuperAdmin_view_admin.html',{'user_registration':user,'designation':designations})

def admindelete(request, id):
    user = user_registration.objects.get(id=id)
    try:
        user.delete()
        return redirect('SuperAdmin_admin_view')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_admin_view')


def SuperAdmin_admin_update(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        user=user_registration.objects.get(id=id)
        branchs=branch_registration.objects.all()

        return render(request,'SuperAdmin_update_admin.html',{'user_registration':user,'branch_registration':branchs})

def SuperAdmin_updatesave(request,id):
        
        if request.method == 'POST':
            usr = user_registration.objects.get(id=id)
            usr.fullname = request.POST.get('aname')
            usr.fathername = request.POST.get('fname')
            usr.dateofbirth = request.POST.get('date')
            usr.gender = request.POST.get('gen')
            usr.mobile = request.POST.get('mob')
            usr.email = request.POST.get('mail')
            usr.alternativeno = request.POST.get('alternative')
            try:
                usr.idproof = request.FILES['idp']
                usr.photo = request.FILES['pic']
            except:
                pass
            
            br_id = request.POST.get("Adminbranch")
            usr.branch_id = br_id
            usr.save()
            return redirect('SuperAdmin_admin_view')








def SuperAdmin_Branch(request):
    return render(request,'SuperAdmin_Branch.html')

def SuperAdmin_AddBranch(request):
    if request.method == 'POST':
        br1 = request.POST['Brname']
        br2 = request.POST['location']
        br3 = request.POST['Brtype']
        br4 = request.POST['Bradmin']
        br5 = request.POST['Bremail']
        br6 = request.POST['Brcontact']
        br7 = request.FILES['img[]']

        new1 = branch_registration(branch_name=br1,location=br2,
                                  branch_type=br3, branch_admin=br4,logo = br7,
                                  email= br5,mobile =br6)
        new1.save()

    return render(request,'SuperAdmin_AddBranch.html')





def SuperAdmin_Viewbranch(request):
    # if 'm_id' in request.session:
    #     if request.session.has_key('m_id'):
    #         m_id = request.session['m_id']
        
    # mem = user_registration.objects.filter(id=m_id)

    branch=branch_registration.objects.all()
    return render(request,'SuperAdmin_Viewbranch.html',{'branch_registration':branch})

def SuperAdmin_Updatebranch(request,id):
    # if 'm_id' in request.session:
    #     if request.session.has_key('m_id'):
    #         m_id = request.session['m_id']
        
    # mem = user_registration.objects.filter(id=m_id)

    branch=branch_registration.objects.get(id=id)
   
    return render(request,'SuperAdmin_Updatebranch.html',{'branch_registration':branch})


def SuperAdmin_branchupdate(request,id):
    if request.method=="POST":
        br=branch_registration.objects.get(id=id)
        br.branch_name=request.POST['brname']
        br.location=request.POST['brlocation']
        br.branch_type=request.POST['brtype']
        br.branch_admin=request.POST['bradmin']
        br.email=request.POST['bremail']
        br.mobile=request.POST['brmobile']
        br.save()
        
        lg=branch_registration.objects.get(id=id)
        try: 
            lg.logo = request.FILES['photo']
            lg.save()
        except:
            br.save()
        
        

    
       

        return redirect('SuperAdmin_Viewbranch')


def SuperAdmin_Branchdelete(request,id):
    branch=branch_registration.objects.get(id=id)
    try:
        
        branch.delete()
        return redirect('SuperAdmin_Viewbranch')
    except:
        messages.success(request, "  Error Occured: It can't be deleted, it used as ForeignKey Constrain !!")
        return redirect('SuperAdmin_Viewbranch')








def SuperAdmin_ReportedissueShow(request,id):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        reported_issues=reported_issue.objects.all()
        branches=branch_registration.objects.get(id=id)
        user=user_registration.objects.filter(branch_id = id)
        return render(request,'SuperAdmin_ReportedissueShow.html',{'branch':branches,'reported_issue':reported_issues,'user_registration':user})
    # else:
    #     return redirect('/')

def SuperAdmin_Reportedissue_department(request):
    # if 'Adm_id' in request.session:
    #     if request.session.has_key('Adm_id'):
    #         Adm_id = request.session['Adm_id']
    #     else:
    #         variable="dummy"
    #     Adm = user_registration.objects.filter(id=Adm_id)
        branch=branch_registration.objects.all()
        file = user_registration.objects.all()
        return render(request, 'SuperAdmin_Reportedissue_department.html',{'branches':branch,'files':file})
    # else:
    #     return redirect('/')

def SuperAdminreply(request,id):
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('SuperAdmin_Reportedissue_department')