from django.shortcuts import render, redirect
from django.http import HttpResponse
#from .forms import ContactForm
from .forms import JournalRecordForm
from .forms import CreateUserForm
from .models import JournalRecord
from django.shortcuts import render
import folium
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect) 
import requests
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


## ---------------Homepage--------------------------------

@login_required(login_url='login')
def FishJournal_detail(request):
    form = JournalRecordForm()

    if request.method == 'POST':
        form = JournalRecordForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry Completed')
        return redirect('fj2')

    # --- Statistics
    records = JournalRecord.objects.all().filter(user=request.user)
    lists = reversed(records)
    total = len(records)
    per = JournalRecord.objects.values('species').annotate(Count('id')).filter(id__count__gt=0, user=request.user)
    largest = records.order_by('-size')[0]

    # --- Map functionality - for loop to find markers
    m = folium.Map(width=600, height=475, location=[49.2827, -123.1207])

    for x in records:
        folium.Marker(
            location=[x.latitude, x.longitude],
            popup=f'{x.size}, {x.species}',
        ).add_to(m)

    m.add_child(folium.LatLngPopup())
    m = m._repr_html_()

    context = {'lists':lists, 'form':form, 'total':total, 'largest':largest, 'per':per, 'm':m}
    return render(request, "form.html", context)

# ---------------logins--------------------------------
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('fj2')
        form = CreateUserForm()
    else:
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, "register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('fj2')
        form = CreateUserForm()
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('fj2')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# ------------------ List View -------------------------------------
@login_required(login_url='login')
def listView(request):
    
    records=reversed(JournalRecord.objects.all())
    context = {'records':records}

    return render(request, 'listview.html', context)

# ------------------ C-R-U-D  -------------------------------------
@login_required(login_url='login')
def detailView(request, id):
    
    detail = JournalRecord.objects.get(id = id)
    context ={'detail':detail}

    return render(request, 'detailview.html', context)

@login_required(login_url='login')
def updateView(request, id):
    
    obj = get_object_or_404(JournalRecord, id=id)
    form = JournalRecordForm(request.POST or None, instance = obj)
    context = {'form':form, 'obj':obj}

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'updateview.html', context)

@login_required(login_url='login')
def delete(request, id):
    
    obj = get_object_or_404(JournalRecord, id=id)
    context = {'obj':obj}

    if request.method=="POST":
        obj.delete()
        return redirect('fj2')

    return render(request, 'deleteview.html', context)
