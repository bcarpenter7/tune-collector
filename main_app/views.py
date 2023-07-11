from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tune


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def tunes_index(request):
    tunes = Tune.objects.all()
    return render(request, 'tunes/index.html', {
        'tunes': tunes
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