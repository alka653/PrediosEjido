from django.db import models

class Propieta(models.Model):
	id_propieta = models.CharField(max_length = 15)
	name = models.CharField(max_length = 30)
	def __unicode__(self):
		return self.id_propieta+' '+self.name

class Predio(models.Model):
	c_catastral = models.CharField(max_length = 15)
	t_ord = models.CharField(max_length = 3)
	t_tot = models.CharField(max_length = 3)
	propieta = models.CharField(max_length = 50)
	e = models.CharField(max_length = 1, blank = True, null = True)
	d = models.CharField(max_length = 1, blank = True, null = True)
	id_propietario = models.CharField(max_length = 15, default = '0')
	dir_predio = models.CharField(max_length = 30)
	hectarea = models.IntegerField(default = 0)
	met2 = models.IntegerField()
	area_con = models.IntegerField(default = 0)
	avaluo_catastral = models.DecimalField(max_digits = 11, decimal_places = 2)
	c_recaja = models.IntegerField(blank = True, null = True)
	f_recaja = models.DateField(auto_now = False, blank = True, null = True)
	v_recaja = models. DecimalField(max_digits = 11, decimal_places = 2, blank = True, null = True)
	id_propieta_fin = models.ForeignKey(Propieta, blank = True, null = True)
	def __unicode__(self):
		return str(self.pk)