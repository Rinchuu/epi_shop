from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'global/homepage.html')

def login(request):
    return render(request, 'global/login.html')

def create_user(request):
    return render(request, 'global/create_user.html')

def shop(request):
    return render(request, 'global/shop.html')
