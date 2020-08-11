# Buildin classes
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Views
from .views import Dashboard,Login,Register,Logout,Home,Profile
from .views import AllCategory,AllPost,AllComment,AllLike
from .middlewares import loginCheck,logoutCheck # Middlewares

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

    # Comment
    path('allcomment', loginCheck(AllComment.as_view()), name="allComment"),
    path('comment',loginCheck(AllComment.loggedInUserComment), name="loggedInUserComment"),
    path('comment/delete/<int:post_id>/<int:comment_id>',loginCheck(AllComment.deleteComment), name="deleteComment"),
    
    # Like & Unlike
    path('post/like/<int:post_id>/',loginCheck(AllLike.like), name="likePost"),
    path('post/unlike/<int:post_id>/',loginCheck(AllLike.unlike), name="unlikePost"),

    # Profile
    path('/<int:profile_id>', loginCheck(Profile.viewProfile), name="profile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
