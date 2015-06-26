from django.shortcuts import render
from collection.models import Thing

# Create your views here.

def index(request):
	things = Thing.objects.all()
	return render(request, 'index.html', {
	'things': things,
})


def index (request):
	#defining the variable
	number = 6

	# adding a string
	thing = "Thing Name"

	# passing the variable to the view.
	things = Thing.objects.all()
	return render(request, 'index.html', {
		'number': number,
		'things': things,
		'thing': things,
		})
	
	