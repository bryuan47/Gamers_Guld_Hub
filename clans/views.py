from django.shortcuts import render
from .models import Clans

# Create your views here.
def index(request):
    return render(request, 'index.html')

def clan(request):
    clan_list = Clans.objects.all()
    return render(request, 'clan_page.html', 
        {'clan_list':clan_list} )



