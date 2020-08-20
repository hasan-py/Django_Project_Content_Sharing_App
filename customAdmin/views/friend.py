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
		try:
			profile_id = request.session["loggedInUser"]["id"]
			reqs = Friend.objects.filter(receiver=profile_id, official=False)
			loggedInUserSendReq = Friend.objects.filter(sender=request.session["loggedInUser"]["id"], official=False)

			if request.GET.get("sender") and request.GET.get("receiver"):
				sender_id = request.GET.get("sender")
				receiver_id = request.GET.get("receiver")
				req = Friend.objects.get(receiver=receiver_id,sender=sender_id,official=False)
				req.official = True
				req.save()
				messages.success(request,"Friend Request Accept")
				return redirect("friendReq")

			if request.GET.get("cancel"):
				deleteId = request.GET.get("cancel")
				senderId = request.GET.get("sender")
				delete = Friend.objects.get(receiver=deleteId,sender=senderId,official=False)
				delete.delete() 
				messages.success(request,"Friend Request Deleted")
				return redirect("friendReq")

			if request.GET.get("addFriend"):
				senderId = request.GET.get("addFriend")
				receiverId = request.GET.get("receiver")
				checkRequestSent = Friend.objects.filter(sender=senderId,receiver=receiverId,official=False)
				if checkRequestSent:
					messages.warning(request,"Request already sent")
					return redirect("profile",senderId)
				else:
					newFriend = Friend.objects.create(
							sender=All_user.objects.get(id=receiverId),
							receiver=All_user.objects.get(id=senderId),
							updated_at=timezone.localtime(timezone.now())
						)
					newFriend.save()
					messages.success(request,"Friend request sent")
					return redirect("profile",senderId)

			return render(request,"Friend/friends-req.html",{"reqs":reqs,"loggedInUserSendReq":loggedInUserSendReq})
		except:
			return redirect("404")