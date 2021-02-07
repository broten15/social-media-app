from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('landing'))

def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            # Log the user in and direct them to the home page
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('feed'))
    
    context = {'form':form}
    return render(request, 'users/register.html', context)