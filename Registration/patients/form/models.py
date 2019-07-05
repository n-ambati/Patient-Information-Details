from django.db import models

# Create your models here.
def prescription_path(instance, filename):
    #name, extension = filename.split(".")
    return "prescription/" + str(filename)

def lab_files_path(instance, filename):
    #name, extension = filename.split(".")
    return "lab_file/" + str(filename)

class Patient(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    telephone = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    profession = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    prescription = models.FileField(upload_to=prescription_path, blank=True)
    lab_file = models.FileField(upload_to=lab_files_path, blank=True)

    def __str__(self):
        return self.first_name
