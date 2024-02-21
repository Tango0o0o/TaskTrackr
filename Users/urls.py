from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from Users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", view=views.register, name="register"),
    path("login/", view=LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", view=LogoutView.as_view(template_name="registration/logout.html"),name="logout"),
    path("profile/edit", view=views.edit_profile, name="edit_profile"),
    path("profile/<int:user_id>",view=views.view_profile,name="view_profile"),
    path("discord-login",  view=views.discord_login, name="discord_login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)