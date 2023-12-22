"""
URL configuration for Villablanca_Francisco_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Villablanca_Francisco_FINAL_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index),
    path('inscritos_class_list/', views.InscritoList.as_view()),
    path('inscritos_class_list/<int:id>/', views.InscritoDetalle.as_view()),
    path('institucion_list/', views.institucion_list),
    path('institucion_list/<int:id>/', views.institucion_detalle),
    path('inscritos_form/', views.inscrito_form),
    path('inscritos_list/', views.inscritos_list),
    path('institucion_form/', views.institucion_form),
    path('datos_personales/', views.datos_autor),
    path('modificar_inscrito/<int:id>/', views.modificar_inscrito),
    path('eliminar_inscrito/<int:id>/', views.eliminar_inscrito),
    path('modificar_institucion/<int:id>/', views.modificar_institucion),
    path('eliminar_institucion/<int:id>/', views.eliminar_institucion)
]
