from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from customAdmin.models import Category


class AllCategory(View):

	# All Category
	def get(self,request):
		if request.GET.get('delete'):
			self.deleteCategory(request,request.GET.get('delete'))

		allCategory = Category.objects.all()
		return render(request,"Category/all-category.html",{"allCategory":allCategory})

	# Add Category
	def post(self,request):
		newCategory = Category(
				name = request.POST.get('categoryName'),
				description = request.POST.get('categoryDiscription'),
				updated_at = timezone.localtime(timezone.now())
			)
		newCategory.save()
		messages.success(request, f"{request.POST.get('categoryName')} added successfully. ")
		return redirect('allCategory')

	# Delete Category
	def deleteCategory(self,request,cat_id):
		cat = Category.objects.get(id=cat_id)
		cat.delete()
		messages.success(request, f"{cat.name} deleted successfully. ")
		return redirect('allCategory')

	# Edit and detail view Category
	def updateCategory(request,cat_id):

		if request.method == "POST":
			editCategory = Category.objects.get(id=cat_id)

			editCategory.name = request.POST.get('categoryName')
			editCategory.description = request.POST.get('categoryDiscription')
			editCategory.updated_at = timezone.localtime(timezone.now())

			editCategory.save()
			messages.success(request,f"{request.POST.get('categoryName')} updated successfully. ")
			return redirect('allCategory')

		category = Category.objects.get(id=cat_id)
		return render(request,"Category/view-category.html",{"category":category})