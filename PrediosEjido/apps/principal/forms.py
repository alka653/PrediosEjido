# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class PredioForm(forms.ModelForm):
	class Meta:
		model = Predio
		fields = '__all__'
		exclude = ('c_recaja', 'f_recaja', 'v_recaja', 'id_propieta_fin')
		widgets = {
			'c_catastral': TextInput(attrs = {'class': 'form-control number-val', 'maxlength': '15', 'required': True}),
			't_ord': TextInput(attrs = {'class': 'form-control number-val', 'maxlength': '3', 'required': True}),
			't_tot': TextInput(attrs = {'class': 'form-control number-val', 'maxlength': '3', 'required': True}),
			'propieta': TextInput(attrs = {'class': 'form-control', 'maxlength': '9', 'required': True}),
			'e': TextInput(attrs = {'class': 'form-control', 'maxlength': '1'}),
			'd': TextInput(attrs = {'class': 'form-control', 'maxlength': '1'}),
			'id_propietario': TextInput(attrs = {'class': 'form-control', 'maxlength': '15', 'required': True}),
			'dir_predio': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'hectarea': TextInput(attrs = {'class': 'form-control number-val'}),
			'met2': TextInput(attrs = {'class': 'form-control number-val', 'required': True}),
			'area_con': TextInput(attrs = {'class': 'form-control number-val'}),
			'avaluo_catastral': TextInput(attrs = {'class': 'form-control number-val', 'maxlength': '9', 'required': True})
		}
		labels = {
			'c_catastral': 'Código Catastral',
			't_ord': 'ORD',
			't_tot': 'TOT',
			'propieta': 'Nombre del Propietario',
			'e': 'E',
			'd': 'D',
			'id_propietario': 'Identificación del Propietario',
			'dir_predio': 'Dirección del Predio',
			'hectarea': 'Tamaño en Hectárea',
			'met2': 'Tamaño en Metros',
			'area_con': 'Tamaño de Área Construida',
			'avaluo_catastral': 'Valor Avaluo Catastral'
		}

class PropietarioVentaForm(forms.Form):
	c_recaja = forms.CharField(label = 'Código Recibo de Caja', widget = forms.TextInput(attrs = {'required': True, 'class': 'form-control number-val'}))
	f_recaja = forms.CharField(label = 'Fecha del Recibo de Caja', widget = forms.TextInput(attrs = {'required': True, 'class': 'form-control datepicker'}))
	v_recaja = forms.CharField(label = 'Valor Recibo de Caja', widget = forms.TextInput(attrs = {'required': True, 'class': 'form-control number-val', 'maxlength': '9'}))
	id_propieta_fin = forms.ModelChoiceField(label = 'Propietario', queryset = Propieta.objects.all(), widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))

class UploadForm(forms.Form):
	file_input = forms.FileField()

	def upload(self):
		val = 0
		text = self.cleaned_data.get('file_input')
		for txt in text.readlines():
			predio_array = []
			val = txt.replace('\n', '').replace(',', '')
			for v in val.split(" "):
				predio_array.append(v)
			predio = Predio(c_catastral = predio_array[0], t_ord = predio_array[1], t_tot = predio_array[2], propieta = predio_array[3].replace('-', ' '), e = predio_array[4], d = predio_array[5], id_propietario = predio_array[6], dir_predio = predio_array[7].replace('-', ' '), hectarea = int(predio_array[8]), met2 = int(predio_array[9]), area_con = int(predio_array[10]), avaluo_catastral = int(predio_array[11]))
			predio.save()
		return "Importación Exitoso"


class PropietaForm(forms.ModelForm):
	class Meta:
		model = Propieta
		fields = '__all__'
		widgets = {
			'id_propieta': TextInput(attrs = {'class': 'form-control', 'maxlength': '15', 'required': True}),
			'name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
		}
		labels = {
			'id_propieta': 'Identificación del propietario',
			'name': 'Nombre Completo del propietario',
		}