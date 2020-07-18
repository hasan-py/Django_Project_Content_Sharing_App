from django.shortcuts import render, redirect
from django.views import View
import datetime

class Home(View):
	DateTime = datetime.datetime.now()
	def get(self,request):
		print('Home')
		return render(request,"base.html",{"datetime":self.DateTime})