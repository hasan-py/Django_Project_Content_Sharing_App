# Buildin classes
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Views
from .views import Dashboard,Login,Register,Logout
from .views import AllCategory

# Middlewares
from .middlewares import loginCheck,logoutCheck

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login & Register
    path('login', logoutCheck(Login.as_view()) , name="login"),
    path('register', logoutCheck(Register.as_view()) , name="register"),

    # Dashboard & logout
    path('', loginCheck(Dashboard.as_view()), name="dashboard"),
    path('logout', loginCheck(Logout.as_view()), name="logout"),

    # Category
    path('categories', loginCheck(AllCategory.as_view()), name="allCategory"),
    path('categories/<int:cat_id>', loginCheck(AllCategory.viewCategory), name="allCategory"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
