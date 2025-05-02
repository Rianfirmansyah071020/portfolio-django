from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

from portfolio.models import Hobi, JenisKelamin, Pengalaman, Project, Pendidikan

# Custom AdminSite
class MyAdminSite(AdminSite):
    site_header = "Panel Admin Web"
    site_title = "Admin Web"
    index_title = "Selamat Datang di Panel Admin"
    enable_nav_sidebar = True


admin_site = MyAdminSite(name='myadmin')

# Admin classes
class HobiAdmin(admin.ModelAdmin):
    list_display = ['hobi', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['hobi']
    list_filter = ['created_at']
    ordering = ['hobi', 'created_at', 'deleted_at']
    fields = ['hobi']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

class JenisKelaminAdmin(admin.ModelAdmin):
    list_display = ['jenis_kelamin', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['jenis_kelamin']
    list_filter = ['created_at']
    ordering = ['jenis_kelamin', 'created_at', 'deleted_at']
    fields = ['jenis_kelamin']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

class PengalamanAdmin(admin.ModelAdmin):
    list_display = ['pengalaman', 'tanggal_mulai', 'tanggal_selesai', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['pengalaman']
    list_filter = ['created_at']
    ordering = ['pengalaman']
    fields = ['pengalaman', 'tanggal_mulai', 'tanggal_selesai']

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

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

# Register models to custom admin site
admin_site.register(Hobi, HobiAdmin)
admin_site.register(JenisKelamin, JenisKelaminAdmin)
admin_site.register(Pengalaman, PengalamanAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(Pendidikan, PendidikanAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
