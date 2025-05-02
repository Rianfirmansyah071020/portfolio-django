from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.utils.safestring import mark_safe


from portfolio.models import Hobi, JenisKelamin, Pengalaman, Project, Pendidikan, Skill, SosialMedia, ProjectImage, Profil

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
    list_filter = ['created_at', 'tanggal_mulai', 'tanggal_selesai']
    ordering = ['pengalaman']
    fields = ['pengalaman', 'tanggal_mulai', 'tanggal_selesai']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

class ProjectImageInline(admin.TabularInline):  # atau StackedInline
    model = ProjectImage
    extra = 2  # jumlah form kosong awal
    max_num = None  # tanpa batas
    fields = ['image']
    show_change_link = True


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'deskripsi', 'link', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['project', 'deskripsi', 'link']
    list_filter = ['created_at']
    ordering = ['project', 'deskripsi', 'link', 'created_at']
    fields = ['project', 'deskripsi', 'link', 'display_images']  # tampilkan di halaman detail
    readonly_fields = ['display_images']  # agar tidak bisa diubah langsung
    list_per_page = 10
    inlines = [ProjectImageInline]

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

    def display_images(self, obj):
        images = obj.images.all()
        if not images:
            return "Tidak ada gambar."
        return mark_safe(''.join([
            f'<img src="{img.image.url}" width="150" style="margin:5px;" />'
            for img in images
        ]))
    display_images.short_description = 'Gambar Terkait'

class PendidikanAdmin(admin.ModelAdmin):
    list_display = ['pendidikan', 'tahun_lulus', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['pendidikan']
    list_filter = ['created_at']
    ordering = ['pendidikan']
    fields = ['pendidikan', 'tahun_lulus']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

class SkillAdmin(admin.ModelAdmin):
    change_list_template = 'admin/portfolio/skill/change_list.html'

    list_display = ['skill', 'gambar_tag',  'created_at', 'deleted_at_display', 'status']
    search_fields = ['skill']
    list_filter = ['created_at']
    ordering = ['skill', 'created_at']
    fields = ['skill', 'gambar', 'gambar_tag']
    readonly_fields = ['gambar_tag']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

    def gambar_tag(self, obj):
        if obj.gambar:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" width="50"  height="auto" />'
                '</a>',
                obj.gambar.url, obj.gambar.url
            )
        return "-"
    gambar_tag.short_description = 'Gambar'



class SosialMediaAdmin(admin.ModelAdmin):
    list_display = ['sosial_media', 'link', 'gambar_tag', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['sosial_media', 'link']
    list_filter = ['created_at']
    ordering = ['sosial_media', 'link', 'created_at']
    fields = ['sosial_media', 'link', 'gambar_tag']
    readonly_fields = ['gambar_tag']
    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

    def gambar_tag(self, obj):
        if obj.gambar:
            return format_html('<a href="{}" target="_blank"><img src="{}" width="70"  height="auto" /></a>', obj.gambar.url, obj.gambar.url) # format_html('<img src="{}" width="100" height="auto" />', obj.gambar.url)
        return "-"
    gambar_tag.short_description = 'Gambar'

class ProfilAdmin(admin.ModelAdmin):
    list_display = ['nama', 'gambar_tag', 'jenis_kelamin', 'tanggal_lahir', 'alamat', 'email', 'no_hp', 'created_at', 'deleted_at_display', 'status']
    search_fields = ['nama', 'jenis_kelamin__nama', 'tanggal_lahir', 'alamat', 'email', 'no_hp', 'deskripsi']
    list_filter = ['created_at']
    ordering = ['nama']
    fields = ['nama', 'jenis_kelamin', 'tanggal_lahir', 'alamat', 'email', 'no_hp', 'deskripsi', 'gambar', 'gambar_preview']
    readonly_fields = ['gambar_preview']  # agar tampil preview saat edit

    list_per_page = 10

    def deleted_at_display(self, obj):
        return obj.deleted_at or "-"
    deleted_at_display.short_description = 'Deleted At'

    def status(self, obj):
        return "Deleted" if obj.deleted_at else "Active"

    def gambar_tag(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="40" height="auto" />', obj.gambar.url)
        return "-"
    gambar_tag.short_description = 'Gambar'

    def gambar_preview(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="100" height="auto" />', obj.gambar.url)
        return "No image"
    gambar_preview.short_description = 'Preview Gambar'







# Register models to custom admin site
admin_site.register(Hobi, HobiAdmin)
admin_site.register(JenisKelamin, JenisKelaminAdmin)
admin_site.register(Pengalaman, PengalamanAdmin)
admin_site.register(Project, ProjectAdmin)
admin_site.register(Pendidikan, PendidikanAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Skill, SkillAdmin)
admin_site.register(SosialMedia, SosialMediaAdmin)
admin_site.register(Profil, ProfilAdmin)
