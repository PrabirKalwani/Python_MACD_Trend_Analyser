from django.shortcuts import render


def home(request):
    return render(request, 'website/home.html')

def learn(request):
    return render(request, 'website/learn.html')

def predict(request):
    return render(request, 'website/predict.html')

def penant(request):
    return render(request, 'website/learn/penant.html')

def flag(request):
    return render(request, 'website/learn/flag.html')

def wedge(request):
    return render(request, 'website/learn/wedge.html')

def ascending(request):
    return render(request, 'website/learn/ascending.html')

def descending(request):
    return render(request, 'website/learn/descending.html')

def symmetrical(request):
    return render(request, 'website/learn/symmetrical.html')

def cup(request):
    return render(request, 'website/learn/cup.html')

def head(request):
    return render(request, 'website/learn/head.html')

def double(request):
    return render(request, 'website/learn/double.html')

def gaps(request):
    return render(request, 'website/learn/gaps.html')

