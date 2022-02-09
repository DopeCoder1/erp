from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"erps/index.html")

def home(request):
    return render(request,"erps/index2.html")
