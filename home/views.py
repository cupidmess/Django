from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('/login')

def login_view(request):
    if request.method == 'POST':
        print("Received POST request")
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(f"Username: {username}, Password: {password}")

        if user is not None:
            print("User authenticated successfully")
            auth_login(request, user)
            print("User logged in, redirecting to index")
            return redirect('/')  # Make sure this points to your `index` view
        else:
            print("Authentication failed")
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        print("GET request received")
        return render(request, 'login.html')

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('/login')
