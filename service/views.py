from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from service.models import Memo

# Create your views here.
def main_view(request):
    memo_list = Memo.objects.all().order_by('-upload_time')

    if request.method == 'POST' and request.user.is_authenticated():
        Memo.objects.create(user=request.user, text=request.POST['memo'])

    return render(request, 'main.html', {'memo_list': memo_list})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

def register_view(request):
    error = None
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = request.POST['email']
            user.save()
            
            login(request, user)
            return redirect('/accounts/profile')
        error = 'Wrong ID or Password mismatch'

    return render(request, 'registration/register.html', {'error': error})