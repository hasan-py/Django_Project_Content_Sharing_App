from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import check_password
from customAdmin.models import All_user,Friend
from django.contrib import messages

class Login(View):

	def get(self,request):
		return render(request,"Auth/login.html")

	def post(self,request):
		loginData = request.POST
		userEmail = All_user.emailExist(loginData["email"])
		if userEmail:
			if check_password(loginData["password"],userEmail.password):
				request.session["id"] = userEmail.id
				request.session["loggedInUser"] = {
					"id":userEmail.id,
					"name":userEmail.name,
					"profile_pic":userEmail.profile_pic.url,
					"role":userEmail.role
				}
				request.session.save()
				return redirect('home')
			else:
				messages.warning(request, "Email or password doesn't match")
				return render(request,'Auth/login.html',{"loginData":loginData})
		else:
			messages.warning(request, "Email or password doesn't match")
			return render(request,'Auth/login.html',{"loginData":loginData})


class Logout(View):

	def get(self,request):
		request.session.clear()
		messages.success(request, "Logout successfully")
		return redirect('login')