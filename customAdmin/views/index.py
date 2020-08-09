from django.shortcuts import render, redirect
from django.views import View
import datetime

from django.contrib import messages
from django.utils import timezone
from customAdmin.models import All_user,Category,Post,Comment,Like

class Dashboard(View):
	DateTime = datetime.datetime.now()
	def get(self,request):
		loggedInUser = All_user.objects.get(id=request.session.get('id'))
		return render(request,"base.html",{"datetime":self.DateTime,"loggedInUser":loggedInUser})


class Home(View):
	def get(self,request):
		categories = Category.objects.all().order_by("name")
		comments = Comment.objects.all()
		likes = Like.objects.all()
		if request.GET.get('category'):
			filterPostById = Post.objects.filter(category=int(request.GET.get('category'))).order_by('-id')
			return render(request, 'home.html',{
				"posts":filterPostById,
				"categories":categories,
				"comments":comments,
				"likes":likes
				})

		context = {
			"posts": Post.objects.all().order_by('-id'),
			"categories": categories,
			"comments":comments,
			"likes":likes
		}
		return render(request, "home.html",context)