from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'main.html')

def register_view(request):
    return render(request, 'registration/register.html')