from django.http import JsonResponse
from django.shortcuts import render

from portfolio.models import Pendidikan, Pengalaman, Profesi, Profil, Project, Skill


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



def skill(request):
    data_skill = list(Skill.objects.filter(deleted_at__isnull=True).values())

    try:
        if data_skill:
            return JsonResponse({
                'data': data_skill,
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


def pendidikan(request):
    data_pendidikan = list(Pendidikan.objects.filter(deleted_at__isnull=True).values())

    try:
        if data_pendidikan:
            return JsonResponse({
                'data': data_pendidikan,
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



def pengalaman(request):
    data_pengalaman = list(Pengalaman.objects.filter(deleted_at__isnull=True).values())

    try:
        if data_pengalaman:
            return JsonResponse({
                'data': data_pengalaman,
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


def project(request):
    try:
        projects = Project.objects.prefetch_related('images').filter(deleted_at__isnull=True)

        data_project = []
        for proj in projects:
            image_data = [
                {
                    'id': img.id,
                    'image_url': img.image.url,
                    'uploaded_at': img.uploaded_at
                }
                for img in proj.images.all()
            ]

            data_project.append({
                'id': proj.id,
                'project': proj.project,
                'deskripsi': proj.deskripsi,
                'link': proj.link,
                'created_at': proj.created_at,
                'updated_at': proj.updated_at,
                'images': image_data
            })

        if data_project:
            return JsonResponse({
                'data': data_project,
                'status': 200,
                'message': 'Success',
                'error': False
            })
        else:
            return JsonResponse({
                'data': [],
                'status': 404,
                'message': 'Data not found',
                'error': True
            })

    except Exception as e:
        return JsonResponse({
            'data': [],
            'status': 500,
            'message': f'Error: {str(e)}',
            'error': True
        })