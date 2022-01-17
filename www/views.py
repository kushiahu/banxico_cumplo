# Django
from django.shortcuts import render

# Utils
from .banxico import Banxico


# Views
def home(request):
	return render(request, 'index.html', {})