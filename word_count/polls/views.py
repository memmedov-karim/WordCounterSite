from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def counter(request):
    sentences=request.GET['text']
    count=len(sentences.split())
    context = {
        'sentences':sentences,
        'count':count,
        
    }
    return render(request,'counter.html',context)
