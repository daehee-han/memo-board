from django.shortcuts import render

# Create your views here.
def main_view(request):
    render(request, 'main.html')