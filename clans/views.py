from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def clan(request):
    return render(request, 'clan_page.html')