from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout #

# Create your views here.

# Displays information about currently-signed-in user:
def index(request):
    if not request.user.is_authenticated: #if user is signed in?:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")





def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] # get username from login form
        password = request.POST["password"] # ditto
        user = authenticate(request, username=username, password=password)
            #Authenticate() function takes a request, checks if username/password are valid, and if so, returns who the USER is
        if user is not None: #authentication was successful...:
            login(request, user) #actually log them in using 'user'
            return HttpResponseRedirect(reverse("index"))
        else: #authentication failed:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })


    return render(request, "users/login.html")

def logout_view(request):
    #pass #tells Python, do nothing.
    logout(request) #call logout() function; then return them to...:
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
