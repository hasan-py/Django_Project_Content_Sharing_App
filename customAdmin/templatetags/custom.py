from django import template
register = template.Library()

@register.filter(name='categorySelected')
def categorySelected(category,cat_name):
	if category == cat_name:
		return True
	else:
		return False