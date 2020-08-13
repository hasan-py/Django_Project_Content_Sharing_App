# This two are for deleting existing image after delete post image
import os
from pathlib import Path

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Post,Category,All_user,Comment,Like,Friend
from django.db.models import Q


class Profile:
	def viewProfile(request,profile_id):
		user = All_user.objects.get(id=profile_id)
		posts = Post.objects.filter(user=profile_id)
		likes = Like.objects.filter(user=profile_id)
		comments = Comment.objects.filter(user=profile_id)
		allCategory = Category.objects.all()
		friends = Friend.objects.filter(Q(receiver=profile_id, official=True) | Q(sender=profile_id, official=True))
		friendReq = Friend.objects.filter(receiver=profile_id,official=False)
		print(friends)
		context = {
			"user":user,
			"posts":posts,
			"likes":likes,
			"comments":comments,
			"allCategory":allCategory,
			"friends":friends,
			"friendReq":friendReq
		}

		if request.method == "POST":
			name = request.POST["name"]
			profile_pic = request.FILES.get("profile_pic")
			if profile_pic:
				if not user.profile_pic.url == "upload/profile_pic/user.png":
					oldProfilePic = Path(os.getcwd()+"/customAdmin/"+f"{user.profile_pic}")
					user.name = name
					user.profile_pic = profile_pic
					user.save()
					os.remove(oldProfilePic)
					request.session["loggedInUser"]["name"] = user.name
					request.session["loggedInUser"]["profile_pic"] = user.profile_pic.url
					request.session.save()
					return render(request, "Profile/index.html",context)
				else:
					user.name = name
					user.profile_pic = profile_pic
					user.save()
					request.session["loggedInUser"]["name"] = user.name
					request.session["loggedInUser"]["profile_pic"] = user.profile_pic.url
					request.session.save()
					return render(request, "Profile/index.html",context)

			else:
				user.name = name
				user.save()
				request.session["loggedInUser"]["name"] = user.name
				request.session.save()
				# request.session["loggedInUser"].profile_pic = user.profile_pic
				return render(request, "Profile/index.html",context)

		return render(request, "Profile/index.html",context)
