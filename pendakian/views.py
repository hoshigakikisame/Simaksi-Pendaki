from django.shortcuts import render, redirect
from .models import Solo, Group
from django.contrib.auth.models import User
from .forms import SoloForm, GroupForm

# Create your views here.
def daftar_solo(request):

	form = SoloForm(request.POST or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			data = form.save(commit=False)
			data.user = User.objects.get(username=request.user)
			data.save()
			return redirect('landing')

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'solo.html', context)

def daftar_group(request):

	form = GroupForm(request.POST or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			data = form.save(commit=False)
			data.user = User.objects.get(username=request.user)
			data.save()
			return redirect('landing')

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'group.html', context)