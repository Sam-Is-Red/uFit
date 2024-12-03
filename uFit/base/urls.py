from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcomePage, name="hello"),
    path("privacy/", views.privacyPage, name="privacy"),
    path("home/", views.homePage, name="home"),
    path("registrationpage/", views.registration_page, name="registrationpage"),
    path("chatpage/", views.chatpage, name="chatpage"),
    path("postpage/", views.postpage, name="postpage"),
    path("profilepage/", views.profilepage, name="profilepage"),
    path("loginpage/", views.login_page, name="loginpage"),
    path("create-message/", views.create_message, name="create-message"),
    path(
        "stream-chat-messages/", views.stream_chat_messages, name="stream-chat-messages"
    ),
]
