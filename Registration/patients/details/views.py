from django.shortcuts import render
from django.http import HttpResponse

from form.models import Patient

# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST.get("id"):
            try:
                ID = request.POST.get("id")
                patient = Patient.objects.get(id=ID)

                p ={"patient": patient}

                return render(request, "details.html", p)
            except:
                return HttpResponse("Enter a valid id")
        else:
            return HttpResponse("Enter a valid id")
    else:
        return HttpResponse("This method is not allowed")
