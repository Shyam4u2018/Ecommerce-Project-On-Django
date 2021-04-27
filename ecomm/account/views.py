from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect


def user_account(request):
	return render(request,'pages/dashboard.html')


def login(request):
	return render(request,'account/login.html')