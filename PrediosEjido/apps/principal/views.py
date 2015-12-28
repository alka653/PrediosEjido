from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from easy_pdf.views import PDFTemplateView
from django.contrib.auth import logout
from django.shortcuts import render
from django.db.models import Sum
from .models import Predio
from .forms import *
import json

@login_required
def home(request):
	return render(request, 'home.html', {'title': 'Bienvenido'})

@login_required
def list_predio(request):
	predios = Predio.objects.all()
	return render(request, 'list-predio.html', {'title': 'Listado de Predios', 'predios': predios})

def view_predio(request, predio_pk):
	predio = Predio.objects.get(pk = predio_pk)
	return render(request, 'show-predio.html', {'title': 'Detalle del Predio', 'predio': predio})

def predio(request, predio_pk = 0):
	try:
		predio = Predio.objects.get(pk = predio_pk)
	except Predio.DoesNotExist:
		predio = predio_pk
	if request.method == 'POST':
		response = {}
		form = PredioForm(request.POST, instance = predio)
		if form.is_valid():
			if predio != 0:
				response['sold'] = True
			else:
				response['sold'] = False
			predio_data = form.save()
			response['pk'] = predio_data.pk
			response['c_catastral'] = predio_data.c_catastral
			response['dir_predio'] = predio_data.dir_predio
			response['hectarea'] = predio_data.hectarea
			response['met2'] = predio_data.met2
			response['avaluo_catastral'] = str(predio_data.avaluo_catastral)
		else:
			response['response'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = PredioForm(instance = predio)
	return render(request, 'form-predio.html', {'title': 'Nuevo Predio', 'predio_val': predio, 'forms': form})

def sold_predio(request, predio_pk):
	predio = Predio.objects.get(pk = predio_pk)
	if request.method == 'POST':
		response = {}
		predio.c_recaja = request.POST['c_recaja']
		predio.f_recaja = request.POST['f_recaja']
		predio.v_recaja = request.POST['v_recaja']
		if request.POST['id_propieta'] != "" and request.POST['id_propieta_fin'] == "":
			propieta = Propieta(id_propieta = request.POST['id_propieta'], name = request.POST['name'])
			propieta.save()
		else:
			propieta = Propieta.objects.get(pk = request.POST['id_propieta_fin'])
		predio.id_propieta_fin = propieta
		predio.save(update_fields = ['c_recaja', 'f_recaja', 'v_recaja', 'id_propieta_fin'])
		response['response'] = predio.pk
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = PropietarioVentaForm()
	return render(request, 'sold-predio.html', {'title': 'Nuevo Propietario de Predio', 'forms': form, 'predio_pk': predio_pk})

def delete_predio(request, predio_pk):
	response = {}
	predio = Predio.objects.get(pk = predio_pk)
	response['response'] = predio.pk
	predio.delete()
	return HttpResponse(json.dumps(response), content_type = 'application/json')

class PredioAllPDFView(PDFTemplateView):
	template_name = "pdf_all_predio.html"

	def get_context_data(self, **kwargs):
		context = super(PredioAllPDFView, self).get_context_data(**kwargs)
		context['option'] = self.kwargs['option']
		if context['option'] == "1":
			predios = Predio.objects.exclude(c_recaja__isnull = True)
		else:
			predios = Predio.objects.all()
		context['predios'] = predios
		context['cont'] = 0
		context['total'] = predios.aggregate(avaluo_catastral_sum = Sum('avaluo_catastral'))
		context['title'] = 'Listado de Predios y Propietarios'
		return context

def upload_data_predio(request):
	message = ""
	type_m = ""
	if request.method == 'POST':
		form = UploadForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			if form.upload():
				message = "Importacion Exitosa"
				type_m = "success"
			else:
				message = "Ha Ocurrido un Error"
				type_m = "danger"
	else:
		form = UploadForm()
	return render(request, 'importer.html', {'title': 'Importar', 'form': form, 'message': message, 'type_m': type_m})

def propietario(request, propieta_pk):
	try:
		propieta = Propieta.objects.get(pk = propieta_pk)
		propieta_val = propieta.pk
	except Propieta.DoesNotExist:
		propieta = propieta_pk
		propieta_val = propieta
	if request.method == 'POST':
		response = {}
		form = PropietaForm(request.POST, instance = propieta)
		if form.is_valid():
			if propieta != 0:
				response['sold'] = True
			else:
				response['sold'] = False
			propieta_data = form.save()
			response['pk'] = propieta_data.pk
			response['id_propieta'] = propieta_data.id_propieta
			response['name'] = propieta_data.name
		else:
			response['response'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = PropietaForm(instance = propieta)
	return render(request, 'form-propieta.html', {'title': 'Nuevo Propietario', 'propieta_val': propieta_val, 'forms': form})

def delete_propieta(request, propieta_pk):
	response = {}
	propieta = Propieta.objects.get(pk = propieta_pk)
	response['response'] = propieta.pk
	propieta.delete()
	return HttpResponse(json.dumps(response), content_type = 'application/json')

@login_required
def list_propieta(request):
	propietas = Propieta.objects.all()
	return render(request, 'list-propieta.html', {'title': 'Listado de Propietarios', 'propietas': propietas})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

@user_passes_test(lambda u: u.is_superuser)
def list_user(request):
	users = User.objects.all()
	return render(request, 'list-user.html', {'title': 'Listado de Usuarios', 'users': users})

def user(request):
	if request.method == 'POST':
		response = {}
		form = UserForm(request.POST)
		if form.is_valid():
			user_data = User.objects.create_user(**form.cleaned_data)
			response['pk'] = user_data.pk
			response['username'] = user_data.username
			response['first_name'] = user_data.first_name
		else:
			response['response'] = "Ha ocurrido un error"
		return HttpResponse(json.dumps(response), content_type = 'application/json')
	else:
		form = UserForm()
	return render(request, 'form-user.html', {'title': 'Nuevo Propietario', 'forms': form})
