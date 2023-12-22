from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from .models import Institucion, Inscrito
from .serializers import InstitucionSerializer, InscritoSerializer
from .forms import InscritoForm, InstitucionForm
# Create your views here.

def Index(request):
    return render(request, 'index.html')

def inscrito_form(request):
    form = InscritoForm()

    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return Index(request)

    data = {'form': form}
    return render(request, 'inscritos_form.html', data)

def inscritos_list(request):
    inscritos = Inscrito.objects.all()
    data = {'object_list': inscritos}
    return render(request, 'inscritos_list.html', data)

def institucion_form(request):
    form = InstitucionForm()

    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return Index(request)

    data = {'form': form}
    return render(request, 'institucion_form.html', data)

def modificar_inscrito(request, id):
    inscrito = Inscrito.objects.get(id=id)
    form = InscritoForm(instance=inscrito)

    if request.method == 'POST':
        form = InscritoForm(request.POST, instance=inscrito)
        if form.is_valid():
            form.save()
            return redirect('/inscritos_list')

    data = {'form': form}
    return render(request, 'inscritos_form.html', data)

def eliminar_inscrito(request, id):
    inscrito = Inscrito.objects.get(id=id)
    inscrito.delete()
    return redirect('/inscritos_list')

def modificar_institucion(request, id):
    institu = Institucion.objects.get(id=id)
    form = InscritoForm(instance=institu)

    if request.method == 'POST':
        form = InscritoForm(request.POST, instance=institu)
        if form.is_valid():
            form.save()
            return redirect('/institucion_list')

    data = {'form': form}
    return render(request, 'institucion_form.html', data)

def eliminar_institucion(request, id):
    institu = Institucion.objects.get(id=id)
    institu.delete()
    return redirect('/institucion_list')

def datos_autor(request):
    data = {
        'nombres': 'Francisco Javier',
        'apellidos': 'Villablanca Keith',
        'rut': '21.238.699-5',
        'carrera' : 'Ingeniería en Informática',
        'asignatura' : 'Programación BackEnd',
        'seccion': 'IEI-170'
    }
    return JsonResponse(data)

#CLASS BASED VIEWS
class InscritoList(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetalle(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            return Http404
    
    def get(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)
    
    def put(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#FUNCION BASED VIEWS
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        institu = Institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(institu)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerializer(institu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        institu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    