from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def learn(request):
    return render(request, 'website/learn.html')

def predict(request):
    return render(request, 'website/predict.html')