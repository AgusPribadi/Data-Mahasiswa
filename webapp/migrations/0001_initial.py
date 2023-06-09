# Generated by Django 4.2.1 on 2023-05-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tanggal_buat", models.DateTimeField(auto_now_add=True)),
                ("nama_awal", models.CharField(max_length=100)),
                ("nama_akhir", models.CharField(max_length=100)),
                ("nim", models.CharField(max_length=20)),
                ("semester", models.CharField(max_length=100)),
                ("kelas", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=255)),
                ("nomor_hp", models.CharField(max_length=20)),
                ("alamat", models.CharField(max_length=300)),
                ("kota", models.CharField(max_length=255)),
                ("provinsi", models.CharField(max_length=200)),
            ],
        ),
    ]
