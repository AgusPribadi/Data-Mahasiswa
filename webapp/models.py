from django.db import models

class Record(models.Model):
    
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    nama_awal = models.CharField(max_length=100)
    nama_akhir = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    semester = models.CharField(max_length=100)
    kelas = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    nomor_hp = models.CharField(max_length=20)
    alamat = models.CharField(max_length=300)
    kota = models.CharField(max_length=255)
    provinsi = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_awal + "   " + self.nama_akhir 
