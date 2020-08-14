from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from customAdmin.models import All_user

class AllUser(View):

	def get(self,request):
		allUser = All_user.objects.all().order_by("-id")
		context = {"allUser":allUser}
		return render(request,"User/all-user.html",context)