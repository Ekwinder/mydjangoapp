from django.shortcuts import render

def name(request):
	return render(request, 'randomname/index.html', {})
