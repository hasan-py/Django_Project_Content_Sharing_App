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
	posts = Post.objects.all(),
	categories = Category.objects.all()
	comments = Comment.objects.all()
	likes = Like.objects.all()
	def get(self,request):

		if request.GET.get('category'):
			filterPostById = Post.objects.filter(category=int(request.GET.get('category')))
			return render(request, 'home.html',{
				"posts":filterPostById,
				"categories":self.categories,
				"comments":self.comments,
				"likes":self.likes
				})

		context = {
			"posts": Post.objects.all(),
			"categories": self.categories,
			"comments":self.comments,
			"likes":self.likes
		}
		print(self.comments)
		return render(request, "home.html",context)