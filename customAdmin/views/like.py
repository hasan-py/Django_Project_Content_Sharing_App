from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from customAdmin.models import Post,Category,All_user,Comment,Like


class AllLike(View):

	def like(request,post_id):
		newLike = Like(
				user = All_user.objects.get(id=request.session.get('loggedInUser')["id"]),
				post = Post.objects.get(id=post_id)
			)
		newLike.save()
		return redirect('allPostById',post_id)

	def unlike(request,post_id):
		like = Like.objects.get(post=post_id,user=request.session.get("loggedInUser")["id"])
		like.delete()
		return redirect('allPostById',post_id)