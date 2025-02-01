from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog_app.models import Blog

User = get_user_model()

@login_required
def home_view(request):
    # Fetch blogs in descending order by creation date
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_app/home.html', {'blogs': blogs})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view') # Redirect to home page after login
        else:
            return HttpResponse("Invalid username or password")
    return render(request, 'auth/login.html')

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone = request.POST['phone']
        profile_picture = request.FILES.get('profile_picture')

        if password == confirm_password:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone=phone,
                profile_picture=profile_picture
            )
            login(request, user)
            return HttpResponse('login')  # Redirect to home page after signup
        else:
            return HttpResponse("Passwords do not match")
    return render(request, 'auth/signup.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'user/profile.html', {'user': user})