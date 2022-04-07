from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo. estas en el index de la encuesta")
