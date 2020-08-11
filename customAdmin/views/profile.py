from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Post,Category,All_user,Comment,Like


class Profile:
	def viewProfile(request,profile_id):
		user = All_user.objects.get(id=profile_id)
		posts = Post.objects.filter(user=profile_id)
		likes = Like.objects.filter(user=profile_id)
		comments = Comment.objects.filter(user=profile_id)
		context = {
			"user":user,
			"posts":posts,
			"likes":likes,
			"comments":comments
		}
		return render(request, "Profile/index.html",context)
