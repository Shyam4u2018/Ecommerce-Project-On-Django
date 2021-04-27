from django.shortcuts import render, redirect,get_object_or_404, HttpResponseRedirect

# Create your views here.

def home(request):
	return render(request,'pages/index.html')
