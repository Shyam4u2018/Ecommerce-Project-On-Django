from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect


def prod(request):
	return render(request,'pages/welcom.html')