from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    pars = {"name": "Fakhru", "city": "Jakarta"}
    return render(request, 'index.html', pars)

def about(request):
    return HttpResponse("<h1>About Page</h1>This is the about view of the InitialProject.</br><a href='/'>Back</a>")

def contact(request):
    return HttpResponse("<h1>Contact Page</h1> Open my portolio at <a href='https://mfakhru.github.io/'>Portofolio</a>")

def shows(request):
    message = request.POST.get('inputText', 'default')
    check_b = request.POST.get('inputCheck', False)
    pars = {"name": "Fakhru", "city": "Jakarta", "message": ""}
    if check_b:
        pars = {"name": "Fakhru", "city": "Jakarta", "message": message}
    return render(request, 'index.html', pars)