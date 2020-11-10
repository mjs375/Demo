from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), #Display info about currently-signed in user
    path("login", views.login_view, name="login"), #login form
    path("logout", views.logout_view, name="logout") #route to allow users to log out

]
