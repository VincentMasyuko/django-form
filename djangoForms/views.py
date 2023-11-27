from django.shortcuts import  render
from djangoForms.forms import StudentForms

def home(request):
    stud=StudentForms
    return render(request,"index.html",{'form':stud})