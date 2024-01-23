from django.shortcuts import render

# Create your views here.
def signup_user(request):
    return render(request, 'user/signup.html')


def login_user(request):
    pass


def logout_user(request):
    pass