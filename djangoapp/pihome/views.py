from django.shortcuts import render
from pihome.models import Action
from pihome.serializers import ActionSerializer
import os


def index(request):
    return render(request, 'pihome/index.html')
