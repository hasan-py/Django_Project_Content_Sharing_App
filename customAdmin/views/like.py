from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from customAdmin.models import Post,Category,All_user,Comment,Like
from django.http import JsonResponse
from django.core import serializers

class AllLike(View):

	def like(request,post_id):
		newLike = Like(
				user = All_user.objects.get(id=request.session.get('loggedInUser')["id"]),
				post = Post.objects.get(id=post_id)
			)
		newLike.save()
		return redirect('allPostById',post_id)

	def unlike(request,post_id):
		loggedInUser = request.session.get("loggedInUser")["id"]
		like = Like.objects.get(post=post_id,user=loggedInUser)
		if Like.hasLike(post_id,loggedInUser):
			like.delete()
			return redirect('allPostById',post_id)
		else:
			return redirect('allPostById',post_id)

	def ajaxReq(request):
		if request.is_ajax and request.method == "POST":
			name = request.POST
			print(name)
			posts = Post.objects.all()
			posts = serializers.serialize('json',posts)
			return JsonResponse({"name":name,"posts":posts})