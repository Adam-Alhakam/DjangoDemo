from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello! This is my TryDjango app.")
