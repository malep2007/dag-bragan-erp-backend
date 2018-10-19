from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Customer Dashboard',
    }
    return render(request, 'customer/index.html', context=data)
