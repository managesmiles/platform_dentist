from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "app_users/index.html")

def index_test(request):
    return render(request, "app_users/index_test.html")

# def login(request):
#     return render(request, "app_users/login.html")

# def register(request):
#     return render(request, "app_users/register.html")

# def index(request):
#     return render(request, "app_users/index.html")