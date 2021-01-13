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

def FishJournal_detail(request):
    records = reversed(JournalRecord.objects.all())
    form = JournalRecordForm()

    if request.method == 'POST':
        form = JournalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry Completed')
        return redirect('fj2')

    context = {'records':records, 'form':form, 'total':total, 'largest':largest, 'per':per, 'm':m}
    return render(request, "form.html", context)

# ---------------logins--------------------------------
def registerPage(request):
    form = CreateUserForm()

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

def listView(request):
    
    records=reversed(JournalRecord.objects.all())
    context = {'records':records}

    return render(request, 'listview.html', context)

# ------------------ C-R-U-D  -------------------------------------

def detailView(request, id):
    
    detail = JournalRecord.objects.get(id = id)
    context ={'detail':detail}

    return render(request, 'detailview.html', context)


def updateView(request, id):
    
    obj = get_object_or_404(JournalRecord, id=id)
    form = JournalRecordForm(request.POST or None, instance = obj)
    context = {'form':form, 'obj':obj}

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, 'updateview.html', context)

def delete(request, id):
    
    obj = get_object_or_404(JournalRecord, id=id)
    context = {'obj':obj}

    if request.method=="POST":
        obj.delete()
        return redirect('fj2')

    return render(request, 'deleteview.html', context)

# ------------------ Map -------------------------------------
    # - Folium Map -
# m = folium.Map(width=600, height=475, location=[49.2827, -123.1207])

# records = JournalRecord.objects.all()

#     # Grabbing flags for all catches
#         #need to add combining of markers when zoom out or too close
# for x in records:
#     folium.Marker(
#         location=[x.latitude, x.longitude],
#         popup=f'{x.size}, {x.species}',
#     ).add_to(m)

# m.add_child(folium.LatLngPopup())

# m = m._repr_html_()



# # -------------------------------------------------------

#     # Calculating statistics
#     #     Total fish caught
# records = JournalRecord.objects.all()

# total = len(records)

#         #Location with most catches

# # Calculate largest fish caught
# def largest():
#     l = JournalRecord.objects.order_by('-size')[:1]
#     for x in l:
#         return (x.size)

# # Calculate per species
# per = JournalRecord.objects.values('species').annotate(Count('id')).order_by().filter(id__count__gt=0)
