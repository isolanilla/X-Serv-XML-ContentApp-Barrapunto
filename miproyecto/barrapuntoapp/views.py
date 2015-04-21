from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import xmlparse

barrapunto = ""

@csrf_exempt
def cms_users_put(request, recurso):

    status = "<p><a href='/admin/logout/'>Logout</a></p>"
    if not request.user.is_authenticated():
       return HttpResponse("<p>No esta logueado <a href='/admin/login/'> Para loguearse</a><p>")
    if request.method == 'GET':
        try:
            pages = Pages.objects.get(name=recurso)
            return HttpResponse("pagina de " + pages.page + status + barrapunto)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Recurso no encontrado" + status + barrapunto)
    elif request.method == 'PUT':
            p = Pages(name=recurso, page=request.body)
            p.save()
            return HttpResponse("Pagina guardada: " + request.body + barrapunto)
    else:
        return HttpResponseNotFound("metodo no disponible")


def update (request):
	global barrapunto
	barrapunto = xmlparse.get_barrapunto()

	return HttpResponse("barrapunto actualizado" + barrapunto)