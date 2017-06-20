from django.shortcuts import render

from service.models import Memo

# Create your views here.
def main_view(request):
    memo_list = Memo.objects.all().order_by('upload_time')

    return render(request, 'main.html', {'memo_list': memo_list})

def register_view(request):
    return render(request, 'registration/register.html')