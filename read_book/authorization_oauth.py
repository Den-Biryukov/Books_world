from django.shortcuts import render


def auth_login_github(request):
    return render(request, 'oauth.html')
