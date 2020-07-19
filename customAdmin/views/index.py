from django.shortcuts import render, redirect
from django.views import View
import datetime

class Dashboard(View):
	DateTime = datetime.datetime.now()
	def get(self,request):
		return render(request,"base.html",{"datetime":self.DateTime})