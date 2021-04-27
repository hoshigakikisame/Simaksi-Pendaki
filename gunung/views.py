from django.shortcuts import render
from .models import Gunung

# Create your views here.
def search(request):

	if 'query' in request.GET:
		query = request.GET['query']
		query = query.strip()
		search_gunung = Gunung.objects.filter(judul__icontains=query).order_by('-upload')
	
		context = {
			'q':query,
			'search_gunung':search_gunung,
		}

		return render(request, 'search.html', context)

	return redirect(index)