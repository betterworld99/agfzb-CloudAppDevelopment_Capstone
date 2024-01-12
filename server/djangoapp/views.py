from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.contrib.auth.forms import UserCreationForm
# from .forms import LoginForm,SignUpForm
from django.contrib.auth.decorators import login_required

# Get an instance of a logger
logger = logging.getLogger(__name__)








def about_view(request):
    return render(request, 'djangoapp/about.html')





# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')



@login_required
def profile_view(request):
    return render(request, 'djangoapp/profile.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('djangoapp:profile')  # Redirect to the profile page upon successful login
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'djangoapp/login.html')



def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('djangoapp:login')
    else:
        form = UserCreationForm()

    return render(request, 'djangoapp/register.html', {'form': form})


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)
        


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

