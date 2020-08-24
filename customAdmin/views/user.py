from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib import messages
from customAdmin.models import All_user

class AllUser(View):

	def get(self,request):
		if request.GET.get('delete'):
			self.deleteUser(request,request.GET.get('delete'))

		allUser = All_user.objects.all().order_by("-id")
		context = {"allUser":allUser}
		return render(request,"User/all-user.html",context)

	# Delete User
	def deleteUser(self,request,profile_id):
		user = All_user.objects.get(id=profile_id)
		user.delete()
		messages.success(request, f" '{user.name}' deleted successfully. ")
		return redirect('allUser')
