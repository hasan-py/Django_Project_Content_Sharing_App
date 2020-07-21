# This two are for deleting existing image after delete post image
import os
from pathlib import Path

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Post
from customAdmin.models import Category


class AllPost(View):

	# All Post
	def get(self,request):
		if request.GET.get('delete'):
			self.deletePost(request,request.GET.get('delete'))

		allPost = Post.objects.all()
		return render(request,"Post/all-post.html",{"allPost":allPost})

	# # Add Post
	# def post(self,request):
	# 	newCategory = Category(
	# 			name = request.POST.get('categoryName'),
	# 			description = request.POST.get('categoryDiscription'),
	# 			updated_at = timezone.localtime(timezone.now())
	# 		)
	# 	newCategory.save()
	# 	messages.success(request, f"{request.POST.get('categoryName')} added successfully. ")
	# 	return redirect('allCategory')

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
			# Image Change Logic
			if request.FILES.get('postImage'):
				editPost = Post.objects.get(id=post_id)
				oldFIle = Path(os.getcwd()+"/customAdmin/"+f"{editPost.image}")
				editPost.image = request.FILES.get('postImage')
				editPost.updated_at = timezone.localtime(timezone.now())
				editPost.save()
				os.remove(oldFIle)
				messages.success(request,"Cover image updated successfully. ")
				return redirect('allPostById',post_id)
			# Without Image
			else:
				editPost = Post.objects.get(id=post_id)
				editPost.title = request.POST.get('postTitle')
				editPost.slug = request.POST.get('postSlug')
				editPost.body = request.POST.get('postBody')
				editPost.updated_at = timezone.localtime(timezone.now())
				editPost.save()
				messages.success(request,f"{request.POST.get('postTitle')} updated successfully. ")
				return redirect('allPostById',post_id)

		post = Post.objects.get(id=post_id)
		allCategory = Category.objects.all()
		options = ""
		for category in allCategory:
			if str(category.name) == str(post.category):
				options = options+f"<option value='{category.name}' selected>{category.name}</option>"
			options = options+f"<option value='{category.name}'>{category.name}</option>"

		return render(request,"Post/view-post.html",{"post":post,"allCategory":allCategory,"options":options})