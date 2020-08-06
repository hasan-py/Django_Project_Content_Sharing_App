# Buildin classes
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Views
from .views import Dashboard,Login,Register,Logout,Home
from .views import AllCategory,AllPost

# Middlewares
from .middlewares import loginCheck,logoutCheck

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login & Register
    path('login', logoutCheck(Login.as_view()) , name="login"),
    path('register', logoutCheck(Register.as_view()) , name="register"),

    # Dashboard & logout
    path('', loginCheck(Dashboard.as_view()), name="dashboard"),
    path('home', loginCheck(Home.as_view()), name="home"),
    path('logout', loginCheck(Logout.as_view()), name="logout"),

    # Category
    path('categories', loginCheck(AllCategory.as_view()), name="allCategory"),
    path('categories/<int:cat_id>/', loginCheck(AllCategory.updateCategory), name="allCategoryById"),

    # Post
    path('posts', loginCheck(AllPost.as_view()), name="allPost"),
    path('posts/<int:post_id>/', loginCheck(AllPost.updatePost), name="allPostById"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
