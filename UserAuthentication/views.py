from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as login_user


# Create your views here.


def login(request):
    """
    Renders a login page or handles user authentication.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered login page or a success message upon successful login.
    """
    if request.method == 'GET':
        return render(request, 'UserAuthentication/login.html')
    elif request.method == 'POST':
        isExisting = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if isExisting:
            login_user(request, isExisting)
            return redirect('index')
        else:
            return redirect('login')
     


