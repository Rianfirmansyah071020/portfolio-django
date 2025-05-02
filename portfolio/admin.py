from django.contrib import admin
from django.utils.html import format_html

from portfolio.models import Hobi, JenisKelamin, Pengalaman, Project, Pendidikan

# Register your models here.



class HobiAdmin(admin.ModelAdmin):
    list_display = ['hobi', 'created_at']
    search_fields = ['hobi']
    list_filter = ['created_at']
    ordering = ['hobi']
    fields = ['hobi']

class JenisKelaminAdmin(admin.ModelAdmin):
    list_display = ['jenis_kelamin', 'created_at']
    search_fields = ['jenis_kelamin']
    list_filter = ['created_at']
    ordering = ['jenis_kelamin']
    fields = ['jenis_kelamin']

class PengalamanAdmin(admin.ModelAdmin):
    list_display = ['pengalaman', 'created_at']
    search_fields = ['pengalaman']
    list_filter = ['created_at']
    ordering = ['pengalaman']
    fields = ['pengalaman', 'tanggal_mulai', 'tanggal_selesai']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'deskripsi', 'gambar_tag', 'link', 'created_at']
    search_fields = ['project', 'deskripsi', 'link']
    list_filter = ['created_at']
    ordering = ['project', 'deskripsi', 'link', 'created_at']
    fields = ['project', 'deskripsi', 'gambar', 'link']

    def gambar_tag(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="100" height="auto" />', obj.gambar.url)
        return "-"
    gambar_tag.short_description = 'Gambar'

class PendidikanAdmin(admin.ModelAdmin):
    list_display = ['pendidikan', 'tahun_lulus', 'created_at']
    search_fields = ['pendidikan']
    list_filter = ['created_at']
    ordering = ['pendidikan']
    fields = ['pendidikan', 'tahun_lulus']




admin.site.register(Hobi, HobiAdmin)
admin.site.register(JenisKelamin, JenisKelaminAdmin)
admin.site.register(Pengalaman, PengalamanAdmin)
admin.site.register(Project, ProjectAdmin)
# admin.site.register(Profil, ProfilAdmin)
admin.site.register(Pendidikan, PendidikanAdmin)