from django.shortcuts import render

# Create your views here.
def header(request):
    return render(request,'home.html')

def nosotros(request):
    return render(request,'nosotros.html')

def cursos(request):
    return render(request,'cursos.html')