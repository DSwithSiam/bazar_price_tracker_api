from django.shortcuts import render
from django.http import HttpResponse

def doc_view(request):
    return render(request, 'doc_api.html')
