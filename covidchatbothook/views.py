
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

def home(request):
    return HttpResponse('<h1>Welcome to the COVIDBot Webhook</h1>')

@csrf_exempt
def world(request):
    
    if (request.method == 'POST'):

        print('Received a post request')

        apiCall = requests.get('https://covid19.mathdro.id/api').json()

        data = {
            'confirmed': apiCall['confirmed']['value'],
            'deaths': apiCall['deaths']['value'],
            'recovered': apiCall['recovered']['value']
        }

        message = "Total number of people in the world affected with COVID19 is {}. There have been {} deaths and {} people recovered.".format(data['confirmed'], data['deaths'], data['recovered'])

        response = ""

        responseObj = {
            "fulfillmentText":  response,
            "fulfillmentMessages": [{"text": {"text": [message]}}],
            "source": ""
        }

        print(responseObj)

        return JsonResponse(responseObj)

    return HttpResponse('OK')