from django.shortcuts import render


def index(request):
	return render(request, 'index.html', {'sample': 'hello world'})

# Create your views here.
