from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def dia_de_hoy(request):
    dia = datetime.now()
    return HttpResponse(f"Hoy es día {dia.day} de {dia.month} de {dia.year} ==> {dia}")

def saludo(request):
    return HttpResponse("Hola mundo, prueba con django!")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre}! es un buen día para practicar Django!")

def probando_template(request):
    
    nombre = "Fabián"
    apellido = "Di Gregorio"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4,8,9,5,7,8]}
    
    # abrimos el archivo index.html
    mi_html = open("./practica/plantillas/index.html")
    # creamos template usando la clase Template
    plantilla = Template(mi_html.read())
    # cerramos el archivo ya que esta cargado en la variable plantilla
    mi_html.close()
    # creamos el contexto con los datos del diccionario
    mi_contexto = Context(diccionario)
    # renderizamos la plantilla
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
    
def usando_loader(request):
    diccionario = {"nombre": "Fabián", "apellido": "Di Gregorio", "notas": [4,8,9,5,7,8]}
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)