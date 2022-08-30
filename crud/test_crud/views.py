from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import Crud
from .serializers import CrudSerializer


def home(request):
    return render(request, 'test_crud/home.html')


class CrudApiList(generics.ListCreateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class CrudApiListUpdate(generics.RetrieveUpdateAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class CrudApiListDelete(generics.RetrieveDestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer


class CrudOneObjectApi(generics.RetrieveAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

# Create your views here.
