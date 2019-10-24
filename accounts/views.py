from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def index(request): 
    # Return the index.html template
    return render(request, 'index.html')

def logout(request): 
    # Logout the user
    auth.logout(request)
    return redirect(reverse('index'))