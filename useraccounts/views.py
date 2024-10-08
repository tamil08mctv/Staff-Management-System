from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.warning(request, "Username or email already taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1
                )
                user.save()
                messages.success(request, "User has been created successfully")
                return redirect('login_user')
        else:
            messages.error(request, "Passwords do not match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.warning(request, "Invalid credentials")
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "User has been logged out successfully")
    return redirect('/')
