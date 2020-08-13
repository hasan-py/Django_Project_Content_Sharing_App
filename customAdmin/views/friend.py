from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from customAdmin.models import Category,All_user,Friend
from django.db.models import Q

class Friends(View):

	def allFriend(request,profile_id):
		allFriend = Friend.objects.filter(Q(receiver=profile_id, official=True) | Q(sender=profile_id, official=True))
		return render(request,"Friend/all-friends.html",{"allFriend":allFriend,"profile_id":profile_id})