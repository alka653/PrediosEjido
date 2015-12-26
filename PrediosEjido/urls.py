from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('PrediosEjido.apps.principal.urls')),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', name = 'login'),
]
