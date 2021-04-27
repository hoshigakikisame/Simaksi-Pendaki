from django.db import models

# Create your models here.
class Gunung(models.Model):
	judul = models.CharField(max_length=100)
	thumbnail = models.ImageField(upload_to='documents/', default="/123.jpg")
	isi = models.TextField()
	upload = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		super(Gunung, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return '{} | {}'.format(self.judul, self.upload)