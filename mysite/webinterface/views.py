from django.shortcuts import render

def web_index(request):
    return render(request, 'webinterface/web_index.html', {})
