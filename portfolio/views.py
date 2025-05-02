from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from .models import Skill

def export_skills_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="skills.pdf"'

    width, height = A4
    p = canvas.Canvas(response, pagesize=A4)
    p.setTitle("Daftar Skill")

    # Judul
    p.setFont("Times-Bold", 16)
    p.drawString(250, height - 60, "Daftar Skill")

    # Ambil data
    skills = Skill.objects.all()

    # Siapkan data untuk tabel
    data = [["No", "Nama Skill"]]
    for idx, skill in enumerate(skills, start=1):
        data.append([str(idx), skill.skill])

    # Buat tabel
    table = Table(data, colWidths=[50, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
        ('FONT', (0, 1), (-1, -1), 'Times-Roman'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ROWHEIGHT', (0, 0), (-1, -1), 20),
    ]))

    # Gambar tabel ke canvas
    table.wrapOn(p, width, height)
    table.drawOn(p, 50, height - 50 - (20 * len(data)))

    p.showPage()
    p.save()
    return response
