from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Transaction
from .serializers import TodoSerializer

# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TodoSerializer

def home(request):
    return HttpResponse("Hello from todoapp")



