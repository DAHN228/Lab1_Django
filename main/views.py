from django.shortcuts import render
from .forms import UserForm


def index(request):
        userform = UserForm()
        return render(request, "main/index.html", {"form": userform})


def about(request):
    return render(request, 'main/about.html')



