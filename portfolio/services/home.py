from django.http import JsonResponse
from django.shortcuts import render

from portfolio.models import Profesi, Profil


def index(request):
    return render(request, 'portfolio/home/index.html')

def profil(request):
    try:
        data_profil = Profil.objects.select_related('jenis_kelamin').filter(deleted_at__isnull=True).first()

        if data_profil:
            return JsonResponse({
                'data': {
                    'id': data_profil.id,
                    'nama': data_profil.nama,
                    'tanggal_lahir': data_profil.tanggal_lahir.isoformat() if data_profil.tanggal_lahir else None,
                    'jenis_kelamin': data_profil.jenis_kelamin.jenis_kelamin if data_profil.jenis_kelamin else None,
                    'alamat': data_profil.alamat,
                    'email': data_profil.email,
                    'no_hp': data_profil.no_hp,
                    'deskripsi': data_profil.deskripsi,
                    'gambar': data_profil.gambar.url if data_profil.gambar else None
                },
                'status': 200,
                'message': 'Success',
                'error': False
            })
        else:
            return JsonResponse({
                'data': {},
                'status': 404,
                'message': 'Data not found',
                'error': True
            })
    except Exception as e:
        return JsonResponse({
            'data': {},
            'status': 500,
            'message': f'Error: {str(e)}',
            'error': True
        })


def profesi(request):
    data_profesi = list(Profesi.objects.filter(deleted_at__isnull=True).values())

    try:
        if data_profesi:
            return JsonResponse({
                'data': data_profesi,
                'status': 200,
                'message': 'Success',
                'error': False
            })
        else:
            return JsonResponse({
                'data': {},
                'status': 404,
                'message': 'Data not found',
                'error': True
            })
    except Exception as e:
        return JsonResponse({
            'data': {},
            'status': 500,
            'message': f'Error: {str(e)}',
            'error': True
        })