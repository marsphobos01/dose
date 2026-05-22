from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Med
from .forms import MedForm
from django.forms.models import model_to_dict

def dashboard(request):
    meds = Med.objects.all()
    return render(request,"tracker/index.html",{"meds":meds})

def view_med(request,med_id):
    pass

def add_med(request):
    if request.method == "POST":
        form = MedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tracker:dashboard")

    else:
        form = MedForm()
        return render(request,"tracker/add_med.html", {"form":form})


def edit_med(request,med_id):
    med = get_object_or_404(Med, id=med_id)
    if request.method == "POST":
        med.name = request.POST.get("name",med.name)
        med.dosage = request.POST.get("dosage",med.dosage)
        med.notes = request.POST.get("notes",med.notes)
        med.save()
    return redirect("tracker:dashboard")

def delete_med(request, med_id):
    med = get_object_or_404(Med, id=med_id)
    if request.method == "POST":
        med.delete()
    return redirect("tracker:dashboard")
