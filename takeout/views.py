from django.shortcuts import render

# Create your views here.
def takeout(request):
    return render(request, 'index.html', {})