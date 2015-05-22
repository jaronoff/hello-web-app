from django.shortcuts import render

# Create your views here.

def index (request):
	#d efining the variable
	number = 12

	# passing the variable to the view.
	return render(request, 'index.html', {
		'number':number,
		})