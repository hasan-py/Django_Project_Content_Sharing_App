from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from customAdmin.models import Category,All_user,Friend
from django.db.models import Q
from django.contrib import messages

class Friends(View):

	def allFriend(request,profile_id):
		allFriend = Friend.objects.filter(Q(receiver=profile_id, official=True) | Q(sender=profile_id, official=True))
		return render(request,"Friend/all-friends.html",{"allFriend":allFriend,"profile_id":profile_id})

	def friendReq(request):
		profile_id = request.session["loggedInUser"]["id"]
		reqs = Friend.objects.filter(receiver=profile_id, official=False)

		if request.GET.get("sender") and request.GET.get("receiver"):
			sender_id = request.GET.get("sender")
			receiver_id = request.GET.get("receiver")
			req = Friend.objects.get(receiver=receiver_id,sender=sender_id,official=False)
			req.official = True
			req.save()
			messages.success(request,"Friend Request Accept")
			return render(request,"Friend/friends-req.html",{"reqs":reqs})

		return render(request,"Friend/friends-req.html",{"reqs":reqs})