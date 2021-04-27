from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Solo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_solo',null=True, blank=True)
	nama = models.CharField(max_length=100)
	nik = models.CharField(max_length=100)

	pilihan_provinsi = (
		('Nanggroe Aceh Darussalam','Nanggroe Aceh Darussalam'),
		('Sumatera Utara','Sumatera Utara'),
		('Sumatera Utara','Sumatera Utara'),
		('Sumatera Barat','Sumatera Barat'),
		('Sumatera Selatan','Sumatera Selatan'),
		('Riau','Riau'),
		('Kepulauan Riau','Kepulauan Riau'),
		('Jambi','Jambi'),
		('Bengkulu','Bengkulu'),
		('Bogor','Bogor'),
		('Bangka Belitung','Bangka Belitung'),
		('Banten','Banten'),
		('DKI Jakarta','DKI Jakarta'),
		('Jawa Timur','Jawa Timur'),
		('Jawa Barat','Jawa Barat'),
		('Jawa Tengah','Jawa Tengah'),
		('DIY','DIY'),
		('Bali','Bali'),
		('Nusa Tenggara Barat','Nusa Tenggara Barat'),
		('Nusa Tenggara Timur','Nusa Tenggara Timur'),
		('Kalimantan Barat','Kalimantan Barat'),
		('Kalimantan Selatan','Kalimantan Selatan'),
		('Kalimantan Timur','Kalimantan Timur'),
		('Kalimantan Utara','Kalimantan Utara'),
		('Kalimantan Tengah','Kalimantan Tengah'),
		('Gorontalo','Gorontalo'),
		('Maluku','Maluku'),
		('Maluku Utara','Maluku Utara'),
		('Papua Barat','Papua Barat'),
		('Papua','Papua'),
		('Sulawesi Barat','Sulawesi Barat'),
		('Sulawesi Selatan','Sulawesi Selatan'),
		('Sulawesi Utara','Sulawesi Utara'),
		('Sulawesi Tengah','Sulawesi Tengah'),
		('Sulawesi Tenggara','Sulawesi Tenggara'),
	)

	provinsi = models.CharField(max_length=100, choices=pilihan_provinsi, default='Bali')
	
	pilihan_tujuan = (
		('Semeru','Semeru'),
		('Arjuno','Arjuno'),
		('Argopuro','Argopuro'),
		('Raung','Raung'),
		('Kawi','Kawi'),
		('Lawu','Lawu'),
		('Sumbing','Sumbing'),
		('Sindoro','Sindoro'),
		('Merbabu','Merbabu'),
		('Merapi','Merapi'),
		('Prau','Prau'),
		('Ciremai','Ciremai'),
		('Papandayan','Papandayan'),
		('Gede','Gede'),
		('Cikuray','Cikuray'),
		('Guntur','Guntur'),
		('Tangkuban Perahu','Tangkuban Perahu'),
		('Salak','Salak'),
		('Dempo','Dempo'),
		('Latimojong','Latimojong'),
		('Agung','Agung'),
		('Kerinci','Kerinci'),
		('Jaya Wijaya','Jaya Wijaya'),
		('Rinjani','Rinjani'),
		('Binaiya','Binaiya'),
		('Bukit Raya','Bukit Raya'),
	)

	tujuan = models.CharField(max_length=100, choices=pilihan_tujuan, default="Semeru")
	naik = models.CharField(max_length=100)
	turun = models.CharField(max_length=100)
	tgl_naik = models.DateField()
	tgl_turun = models.DateField()
	email = models.EmailField()
	tlp = models.BigIntegerField()

	status = (
		('waiting','Menunggu Konfirmasi'),
		('confirmed', 'Sudah dikonfirmasi'),
		('not_confirmed', 'Tidak dikonfirmasi'),
	)

	konfirmasi = models.CharField(max_length=100, choices=status, default='waiting')

	def save(self, *args, **kwargs):
		super(Solo, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return "{} | {} | {}".format(self.nama, self.nik, self.konfirmasi)

class Group(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_group',null=True, blank=True)
	jumlah_pendaki = models.IntegerField()
	nama = models.CharField(max_length=100)
	nik = models.CharField(max_length=100)
	pilihan_provinsi = (
		('Nanggroe Aceh Darussalam','Nanggroe Aceh Darussalam'),
		('Sumatera Utara','Sumatera Utara'),
		('Sumatera Utara','Sumatera Utara'),
		('Sumatera Barat','Sumatera Barat'),
		('Sumatera Selatan','Sumatera Selatan'),
		('Riau','Riau'),
		('Kepulauan Riau','Kepulauan Riau'),
		('Jambi','Jambi'),
		('Bengkulu','Bengkulu'),
		('Bogor','Bogor'),
		('Bangka Belitung','Bangka Belitung'),
		('Banten','Banten'),
		('DKI Jakarta','DKI Jakarta'),
		('Jawa Timur','Jawa Timur'),
		('Jawa Barat','Jawa Barat'),
		('Jawa Tengah','Jawa Tengah'),
		('DIY','DIY'),
		('Bali','Bali'),
		('Nusa Tenggara Barat','Nusa Tenggara Barat'),
		('Nusa Tenggara Timur','Nusa Tenggara Timur'),
		('Kalimantan Barat','Kalimantan Barat'),
		('Kalimantan Selatan','Kalimantan Selatan'),
		('Kalimantan Timur','Kalimantan Timur'),
		('Kalimantan Utara','Kalimantan Utara'),
		('Kalimantan Tengah','Kalimantan Tengah'),
		('Gorontalo','Gorontalo'),
		('Maluku','Maluku'),
		('Maluku Utara','Maluku Utara'),
		('Papua Barat','Papua Barat'),
		('Papua','Papua'),
		('Sulawesi Barat','Sulawesi Barat'),
		('Sulawesi Selatan','Sulawesi Selatan'),
		('Sulawesi Utara','Sulawesi Utara'),
		('Sulawesi Tengah','Sulawesi Tengah'),
		('Sulawesi Tenggara','Sulawesi Tenggara'),
	)

	provinsi = models.CharField(max_length=100, choices=pilihan_provinsi, default='Bali')
	
	pilihan_tujuan = (
		('Semeru','Semeru'),
		('Arjuno','Arjuno'),
		('Argopuro','Argopuro'),
		('Raung','Raung'),
		('Kawi','Kawi'),
		('Lawu','Lawu'),
		('Sumbing','Sumbing'),
		('Sindoro','Sindoro'),
		('Merbabu','Merbabu'),
		('Merapi','Merapi'),
		('Prau','Prau'),
		('Ciremai','Ciremai'),
		('Papandayan','Papandayan'),
		('Gede','Gede'),
		('Cikuray','Cikuray'),
		('Guntur','Guntur'),
		('Tangkuban Perahu','Tangkuban Perahu'),
		('Salak','Salak'),
		('Dempo','Dempo'),
		('Latimojong','Latimojong'),
		('Agung','Agung'),
		('Kerinci','Kerinci'),
		('Jaya Wijaya','Jaya Wijaya'),
		('Rinjani','Rinjani'),
		('Binaiya','Binaiya'),
		('Bukit Raya','Bukit Raya'),
	)

	tujuan = models.CharField(max_length=100, choices=pilihan_tujuan, default="Semeru")
	naik = models.CharField(max_length=100)
	turun = models.CharField(max_length=100)
	tgl_naik = models.DateField()
	tgl_turun = models.DateField()
	email = models.EmailField()
	tlp = models.BigIntegerField()
	
	status = (
		('waiting','Menunggu Konfirmasi'),
		('confirmed', 'Sudah dikonfirmasi'),
		('not_confirmed', 'Tidak dikonfirmasi'),
	)

	konfirmasi = models.CharField(max_length=100, choices=status, default='waiting')

	def save(self, *args, **kwargs):
		super(Group, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return "{} | {} | {}".format(self.nama, self.nik, self.konfirmasi)