from django.http import JsonResponse
from django.shortcuts import render

from portfolio.models import Profil


def index(request):
    return render(request, 'portfolio/home/index.html')

def profil(request):
    dataProfil = Profil.objects.all()

    try:
        return JsonResponse({
        'data': list(dataProfil.values()),
        'status': 200,
        'message': 'Success',
        'error': False
        })
    except:
            return JsonResponse({
            'data': [],
            'status': 200,
            'message': 'Success',
            'error': False
        })