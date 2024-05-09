#from django.urls import path, include
#from api import views

#urlpatterns=[
#    path('',views.index, name="index"),
#]

#una api rest con django rest framework
from rest_framework import routers
from .api import ApiViewSet

ruta = routers.DefaultRouter()
ruta.register('api/empleados', ApiViewSet, 'api')

urlpatterns = ruta.urls
