from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
		my_dict = {'help_info': 'Help me please!'}
		return render(request, 'second_app/index.html', context=my_dict)