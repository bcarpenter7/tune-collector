from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tune


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def tunes_index(request):
    tunes = Tune.objects.order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'All'
    })

def tunes_index_d(request):
    tunes = Tune.objects.filter(key='D').order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'D'
    })

def tunes_index_a(request):
    tunes = Tune.objects.filter(key='A').order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'A'
    })

def tunes_index_g(request):
    tunes = Tune.objects.filter(key='G').order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'G'
    })

def tunes_index_c(request):
    tunes = Tune.objects.filter(key='C').order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'C'
    })


def tunes_detail(request, tune_id):
    tune = Tune.objects.get(id=tune_id)
    return render(request, 'tunes/detail.html', {
    'tune': tune
})

class TuneCreate(CreateView):
    model = Tune
    fields = '__all__'

class TuneUpdate(UpdateView):
    model = Tune
    fields = '__all__'

class TuneDelete(DeleteView):
    model = Tune
    success_url = '/tunes'