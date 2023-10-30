from django.urls import path 
from core.views import chat_page
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_page, name="chat-page"),
    path("auth/login/", LoginView.as_view(template_name="login.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
