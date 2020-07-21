from django import template
register = template.Library()

@register.filter(name='categorySelected')
def categorySelected(categories,cat_name):
	text = ""
	for category in categories:
		if category.name == cat_name:
			text = text+f"<option value='{category.name}' selected>{category.name}</option>"
		text = text+f"<option value='{category.name}'>{category.name}</option>"

	return text