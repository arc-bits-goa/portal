from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from django.views.decorators.csrf import csrf_protect
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.utils.timezone import make_aware
from django.core.mail import send_mail
from django.conf import settings
import xlrd, xlwt
from braces import views
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import ProjectForm


def is_hod(user):
    return False if not Hod.objects.filter(user=user) else True

def is_faculty(user):
     return False if not Faculty.objects.filter(user=user) else True
def index(request):
    return render(request, 'home1.html',{})


def login_success(request):
    return HttpResponse("Success!")

@login_required
@user_passes_test(is_faculty)
def faculty(request):
    faculty = Faculty.objects.filter(user=request.user)
    context ={
        'faculty' : faculty,
    }
    return render(request, "faculty.html",)


@csrf_protect
def loginform(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
                return redirect('/admin')
        if Hod.objects.filter(user=request.user):
            return redirect('/hod')
        if Faculty.objects.filter(user=request.user):
            return redirect('/project')
        return redirect('/')

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:
                return redirect('/admin')
            if Hod.objects.filter(user=request.user):
                return redirect('/hod')
            if Faculty.objects.filter(user=request.user):
                return redirect('/project')
            return redirect('student')
        else:
            messages.add_message(request, messages.INFO,  "Incorrect username or password", extra_tags='red')
            print('Not able to authenticate')

    return render(request, "sign-in.html", {})


@login_required
def logoutform(request):
    logout(request)
    return render(request, "logout.html", {})

@login_required
@user_passes_test(is_hod)
def hod(request):
    hod = Hod.objects.get(user=request.user)
    projects = Project.objects.filter(department=hod.department).order_by('approved', '-id')
    context = {
        'option':1,
        'hfuser': hod,
        'project': projects,
    }
    postContext = {
            'projects':projects
        }
    return render(request, "hod.html", dict(context, **postContext))

# @login_required
# @user_passes_test(is_faculty)
# def faculty(request):
#     faculty = Faculty.objects.filter(user=request.user)
#     return render(request, "hostelsuperintendent.html", context)
@login_required
@user_passes_test(is_faculty)
def project(request):
    faculty = Faculty.objects.get(user=request.user)
    form = ProjectForm()
    web = 'base.html'
    if request.user is not None:
            login(request, request.user)
            if Hod.objects.filter(user=request.user):
                web ='hodbase.html'
    context = {
        'option' : 0,
        'hfuser': faculty,
        'form': form,
        'web':web
    }

    projectContext = {
        'projects': Project.objects.filter(faculty=faculty),
    }

    if request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            projectform = form.save(commit=False)
            projectform.faculty = faculty
            # print(request.POST.get('consent'))
            projectform.save()

            context = {
                'option': 1,
            }
        else:
            context = {
                'option': 2,
                'form': form
            }
            print(form.errors)
    return render(request, "project.html", dict(context, **projectContext))

@login_required
@user_passes_test(is_hod)
def hodprojectapprove(request, project):
    project = Project.objects.get(id=project)
    hod = Hod.objects.get(user=request.user)

    # leaves = Leave.objects.filter(student=leave.student)

    context = {
        'option': 2,
        'hod': hod,
        'project': project,
        'faculty': project.faculty
    }

    if request.POST:
        approved = request.POST.getlist('group1')
        print(approved)
        
        if '1' in approved:
            project.approved=True
            project.disapproved = False
            project.inprocess = False
        elif '2' in approved:
            project.disapproved=True
            project.approved = False
            project.inprocess = False
        else:
            project.inprocess = True
            project.approved = False
            project.disapproved = False
        project.save()
        return redirect('hod')

    return render(request, "hod.html", context)


