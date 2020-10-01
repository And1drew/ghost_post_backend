from django.shortcuts import render
from boastOrRoast.models import BoastOrRoast

# Create your views here.
def index(request):
    data = BoastOrRoast.objects.all()
    return render(request, 'index.html', {'data': data})