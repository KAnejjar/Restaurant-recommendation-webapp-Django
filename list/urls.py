from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^home/(?P<pk>\d+)/$', views.index2, name='index2'),#user connecté
    url(r'^plats/(?P<pk>\d+)/$', views.plat_list, name='plat_list'),#non connecté
    url(r'^plats/(?P<pk>\d+)/2$', views.plat_list2, name='plat_list2'),#connecté
    url(r'(?P<pk>\d+)/$', views.rest_detail,name='rest_detail'),#user connecté
    url(r'(?P<pk>\d+)/2$', views.rest_detail2, name='rest_detail2'),#non connecté
    url(r'acount/create/', views.create_acount,name='create_acount'),#non connecté
    url(r'acount/login/', views.login,name='login'),
    url(r'acount/logout/', views.logout,name='logout'),
    url(r'^about/$', views.about, name='about'),#non connecté
    url(r'^about/2$', views.about2, name='about2'),#connecté
    url(r'^listing/$', views.listing, name='listing'),#non connecté
    url(r'^listing/2$', views.listing2, name='listing2'),#connecté
    url(r'^meilleurs/$', views.meilleurs, name='meilleurs'),#non connecté
    url(r'^meilleurs/2$', views.meilleurs2, name='meilleurs2'),#connecte


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)