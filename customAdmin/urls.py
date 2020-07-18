from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import Home,Login,Register

from .middlewares import authMiddlware


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authMiddlware(Home.as_view()), name="home"),
    path('login', Login.as_view() , name="login"),
    path('register', Register.as_view() , name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
