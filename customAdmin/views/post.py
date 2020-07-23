# This two are for deleting existing image after delete post image
import os
from pathlib import Path

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Post
from customAdmin.models import Category
from customAdmin.models import All_user


class AllPost(View):

	# All Post
	def get(self,request):
		if request.GET.get('delete'):
			self.deletePost(request,request.GET.get('delete'))

		allPost = Post.objects.all()
		allCategory = Category.objects.all()
		allUser = All_user.objects.all()
		context = {"allPost":allPost,"allCategory":allCategory,"allUser":allUser}
		return render(request,"Post/all-post.html",context)

	# Add Post
	def post(self,request):

		postData = request.POST
		newPost = Post(
				title = postData["postTitle"],
				slug = postData["postSlug"],
				body = postData["postBody"],
				category = Category.objects.get(id=postData["postCategory"]),
				image = request.FILES.get('postImage'),
				user_id = postData["postUser"],
				# user_id = request.session.get('id'),
				updated_at = timezone.localtime(timezone.now())
			)
		newPost.save()
		messages.success(request, "Post Published successfully. ")
		return redirect('allPost')

	# Delete Post
	def deletePost(self,request,post_id):
		post = Post.objects.get(id=post_id)
		oldFIle = Path(os.getcwd()+"/customAdmin/"+f"{post.image}")
		post.delete()
		os.remove(oldFIle)
		messages.success(request, f" '{post.title}' deleted successfully. ")
		return redirect('allPost')

	# Edit and detail view Post
	def updatePost(request,post_id):
		if request.method == "POST":
			editPost = Post.objects.get(id=post_id)
			# Image Change Logic
			if request.FILES.get('postImage'):
				oldFIle = Path(os.getcwd()+"/customAdmin/"+f"{editPost.image}")
				editPost.image = request.FILES.get('postImage')
				editPost.updated_at = timezone.localtime(timezone.now())
				os.remove(oldFIle)
			# Without Image
			if not request.FILES.get('postImage') or request.FILES.get('postImage'):
				editPost.title = request.POST.get('postTitle')
				editPost.slug = request.POST.get('postSlug')
				editPost.body = request.POST.get('postBody')
				# Creating Category Intance by Category Id | Because forienKey must need an object
				editPost.category = Category.objects.get(id=request.POST.get('postCategory'))
				editPost.updated_at = timezone.localtime(timezone.now())

			editPost.save()
			messages.success(request,f"({request.POST.get('postTitle')}) updated successfully. ")
			return redirect('allPostById',post_id)

		post = Post.objects.get(id=post_id)
		allCategory = Category.objects.all()
		return render(request,"Post/view-post.html",{"post":post,"allCategory":allCategory})