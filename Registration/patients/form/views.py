from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient

# Create your views here.
def index(request):
    if request.method == "POST":
        patient = Patient()
        patient.id = request.POST.get("id")
        patient.first_name = request.POST.get("firstname")
        patient.last_name = request.POST.get("lastname")
        patient.age = request.POST.get("age")
        patient.sex = request.POST.get("sex")
        patient.telephone = request.POST.get("telephone")
        patient.city = request.POST.get("city")
        patient.profession = request.POST.get("profession")
        patient.blood_group = request.POST.get("blood-group")
        patient.pregnancy = request.POST.get("pregnancy")
        patient.prescription = request.FILES.get("prescription")
        patient.lab_file = request.FILES.get("lab-file")
        patient.save()

        return HttpResponse("<h1>Success!</h1>")
    else:
        return render(request, "index.html")
