from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("Hello World. You're at the AppCoder index.")

def cursos(request):
    return HttpResponse("Hello World. You're at the AppCoder cursos.")

def profesores(request):
    return HttpResponse("Hello World. You're at the AppCoder profesores.")

def estudiantes(request):
    return HttpResponse("Hello World. You're at the AppCoder entregables.")

def entregables(request):
    return HttpResponse("Hello World. You're at the AppCoder entregables.")
