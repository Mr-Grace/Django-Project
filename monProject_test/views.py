from django.http import HttpResponse

def erreur404(request, exception):
    return HttpResponse("404: Page introuvable")

def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1> ')