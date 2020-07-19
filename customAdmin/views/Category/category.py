from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from customAdmin.models import Category

class AllCategory(View):

	def deleteCategory(self,request,cat_id):
		cat = Category.objects.get(id=cat_id)
		cat.delete()
		messages.success(request, "Category delete successfully")
		return redirect('allCategory')

	def viewCategory(self,request,cat_id):
		if request.method == "GET":
			category = Category.objects.get(id=cat_id)
			return render(request,"Category/view-category.html",{"category":category})

	def get(self,request):
		if request.GET.get('delete'):
			self.deleteCategory(request,request.GET.get('delete'))

		allCategory = Category.objects.all()
		return render(request,"Category/all-category.html",{"allCategory":allCategory})
