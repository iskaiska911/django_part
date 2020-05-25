from django.shortcuts import render

def main(request):
    return render(request, "index.html")

def study(request):
    return render(request, "study.html")

def work(request):
    return render(request, "work.html")

# Create your views here.
