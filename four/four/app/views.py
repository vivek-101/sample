from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def home(request):
    return render(request,'app/home.html')

def refrence(request):
    return render(request,'app/refrence.html')
