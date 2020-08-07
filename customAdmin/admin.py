from django.contrib import admin
from .models import All_user,Category,Post,Comment,Like
from django.contrib.auth.models import User,Group

# Unregister all buildin system
admin.site.unregister(User)
admin.site.unregister(Group)

# Register all custom system
admin.site.register(All_user)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
