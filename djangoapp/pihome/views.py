from django.shortcuts import render
from django.http import JsonResponse
from pihome.models import Action
from django.utils import timezone
import os
import paho.mqtt.client as mqtt


def index(request):
    return render(request, 'pihome/index.html')

def lightRoom(request):
    if request.method == 'POST':
        mqtt_client = mqtt.Client(client_id='djangoapp', protocol=mqtt.MQTTv5)
        mqtt_client.connect('localhost', 1883, 60)
        mqtt_client.publish('cmnd/messages/POWER', 'TOGGLE')



        return JsonResponse({'message': 'Light toggled and action saved'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

