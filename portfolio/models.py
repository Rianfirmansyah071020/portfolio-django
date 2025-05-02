from django.db import models
from numpy import delete
from django.utils import timezone


# Create your models here.
class JenisKelamin(models.Model):
    site_header = "Panel Admin Web"
    site_title = "Admin Web"
    index_title = "Selamat Datang di Panel Admin"
    jenis_kelamin = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.jenis_kelamin

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class Hobi(models.Model):
    hobi = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.hobi

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class Pendidikan(models.Model):
    pendidikan = models.CharField(max_length=50)
    tahun_lulus = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.pendidikan

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class Pengalaman(models.Model):
    pengalaman = models.CharField(max_length=50)
    tanggal_mulai = models.DateField(null=True)
    tanggal_selesai = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.pengalaman

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class Skill(models.Model):
    skill = models.CharField(max_length=50)
    gambar = models.ImageField(upload_to='media/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.skill

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()




class Project(models.Model):
    project = models.CharField(max_length=50)
    deskripsi = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.project

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/project_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gambar {self.project.project}"

class SosialMedia(models.Model):
    sosial_media = models.CharField(max_length=50)
    link = models.URLField(null=True)
    gambar = models.ImageField(upload_to='media/images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def __str__(self):
        return self.sosial_media

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def image_tag(self, obj):
        if obj.gambar:
            return format_html('<img src="{}" width="100"/>', obj.gambar.url)
        return "-"
    image_tag.short_description = 'Preview'


class Profil(models.Model):
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.ForeignKey(JenisKelamin, on_delete=models.CASCADE)
    tanggal_lahir = models.DateField(null=True)
    alamat = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    no_hp = models.CharField(max_length=15, null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    gambar = models.ImageField(upload_to='media/images/')
    created_at = models.DateTimeField(auto_now_add=True)  # Diisi saat pertama kali dibuat
    updated_at = models.DateTimeField(auto_now=True)      # Diisi setiap kali di-update
    deleted_at = models.DateTimeField(null=True, blank=True)  # Diisi hanya saat soft delete

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.nama