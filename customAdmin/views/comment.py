from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Post,Category,All_user,Comment,Like


class AllComment(View):

	def loggedInUserComment(request):
		if request.method == "POST":
			commentData = request.POST
			print(request.session.get('loggedInUser')["id"])
			newComment = Comment(
					body = commentData["body"],
					user = All_user.objects.get(id=request.session.get('loggedInUser')["id"]),
					post = Post.objects.get(id=commentData["postId"]),
					updated_at = timezone.localtime(timezone.now())
				)
			newComment.save()
			messages.success(request, "Your comment published")
			return redirect('allPostById',commentData["postId"])

	def deleteComment(request,comment_id,post_id):
		comment = Comment.objects.get(id=comment_id)
		comment.delete()
		messages.success(request, "Your comment deleted")
		return redirect('allPostById',post_id)