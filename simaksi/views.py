from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from pendakian.models import Solo, Group


def index(request):

	if request.user.is_authenticated:
		pendakian_solo = Solo.objects.filter(user=request.user)
		pendakian_group = Group.objects.filter(user=request.user)
		context = {
			'pendakian_solo':pendakian_solo,
			'pendakian_group':pendakian_group,
		}
		return render(request, "home.html", context)

	return render(request, "Pendaki.html")

def view_login(request):
	print(request)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			print("login berhasil")
			return redirect(index)
		else:
			print("gagal login")
	return render(request, "login.html")

def register(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.create_user(username=username, password=password)
		if user:
			print('sukses')
			return redirect(view_login)
		else:
			print('gagal')

	return render(request, "logindaftar.html")

def info_pendakian(request, info):
	if info == "persyaratan":
		return render(request, "pa.html")
	elif info == "istilah":
		return render(request, "istilahx.html")
	elif info == "prepare":
		return render(request, "prepare.html")
	else:
		return redirect('home')

def bukti_solo(request):
	if request.user.is_authenticated:
		pendakian_solo = Solo.objects.filter(user=request.user)
		context = {
			'pendakian_solo':pendakian_solo,
		}
		return render(request, "bukti_solo.html", context)

	return render(request, "Pendaki.html")

def bukti_group(request):
	if request.user.is_authenticated:
		pendakian_group = Group.objects.filter(user=request.user)
		context = {
			'pendakian_group':pendakian_group,
		}
		return render(request, "bukti_group.html", context)

	return render(request, "Pendaki.html")

def logout_views(request):
	logout(request)
	return redirect(index)
