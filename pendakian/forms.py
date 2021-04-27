from django import forms
from .models import Solo, Group

class SoloForm(forms.ModelForm):
	class Meta:
		model = Solo
		fields = ['nama', 'nik', 'provinsi', 'tujuan', 'naik', 'turun', 'tgl_naik', 'tgl_turun', 'email', 'tlp']


class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['jumlah_pendaki', 'nama', 'nik', 'provinsi', 'tujuan', 'naik', 'turun', 'tgl_naik', 'tgl_turun', 'email', 'tlp']