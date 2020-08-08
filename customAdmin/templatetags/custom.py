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
