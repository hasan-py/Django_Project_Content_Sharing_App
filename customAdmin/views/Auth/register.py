import re
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from customAdmin.models import All_user
from django.contrib import messages

class Register(View):
	def get(self,request):
		return render(request,"Auth/register.html")

	def post(self,request):
		registerDetails = request.POST
		error = self.validateData(registerDetails)

		if len(error)>0:
			return render(request,"Auth/register.html",{"error":error,"oldData":registerDetails})
		if All_user.emailExist(registerDetails["email"]):
			error.append("Email already exits")
			print(error)
			return render(request,"Auth/register.html",{"error":error,"oldData":registerDetails})
		else :
			newUser = All_user(
				name=registerDetails["firstName"]+" "+registerDetails["lastName"],
				email=registerDetails["email"],
				password=make_password(registerDetails["password"]),
				profile_pic="./upload/profile_pic/user.png",
				role="admin",
				updated_at = timezone.localtime(timezone.now())
			)
			newUser.save()
			messages.success(request, 'Register successfully. Login please')
			return redirect('login')

	def validateData(self,obj):
		regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
		error = []
		if not obj["firstName"] or not obj["lastName"] or not obj["email"] or not obj["password"] or not obj["confirmPassword"]:
			error.append("Please insert all filed")

		elif len(obj["firstName"])<5 and len(obj["firstName"])>13 :
			error.append("First name must be 5-13 charecter")

		elif len(obj["lastName"])<5 and len(obj["lastName"])>10 :
			error.append("Last name must be 5-10 charecter")

		elif len(obj["password"])<8 or len(obj["confirmPassword"])<8 :
			error.append("Password must be 8 charecter")

		elif(not re.search(regex,obj["email"])):
			error.append("Please insert a valid email")

		elif not obj["password"] == obj["confirmPassword"]:
			error.append("Password doesn't match")

		return error