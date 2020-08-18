from django import template
register = template.Library()

@register.filter(name='categorySelected')
def categorySelected(category,cat_name):
	if category == cat_name:
		return True
	else:
		return False

@register.filter(name='countLC')
def countLC(dict,id):
	newList = []
	for i in dict:
		if i.post.id == id:
			newList.append(i.post.id)
	return len(newList)
	
@register.filter(name='hasLike')
def hasLike(allLike,loggedInUserId):
	for like in allLike:
		if like.user.id == loggedInUserId:
			return True
	return False


@register.filter(name='hasFriend')
def hasFriend(friendList,loggedInUserId):
	for friend in friendList:
		if friend.receiver.id == loggedInUserId or friend.sender.id == loggedInUserId:
			return True
	return False

@register.filter(name='loggedInUserReqFriend')
def loggedInUserReqFriend(friendList,profile_id):
	for friend in friendList:
		if friend.sender.id == profile_id:
			return True
	return False
