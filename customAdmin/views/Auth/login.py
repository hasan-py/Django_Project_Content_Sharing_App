from django.shortcuts import render, redirect
from django.views import View

class Login(View):
	def get(self,request):
		return render(request,"Auth/login.html")