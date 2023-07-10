from django.shortcuts import render


# Add this cats list below the imports
tunes = [
  {'name': 'Billy in the Lowground', 'key': 'C', 'fiddler': 'Lowe Stokes'},
  {'name': 'Sugar in the Gourd', 'key': 'A', 'fiddler': 'Clayton McMichen'},
  {'name': 'Hell Broke Loose in Georgia', 'key': 'C', 'fiddler': 'Burt Layne'},
  {'name': 'Arkansas Traveler', 'key': 'D', 'fiddler': 'Gid Tanner'},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

def tunes_index(request):
    return render(request, 'tunes/index.html', {
        'tunes': tunes
    })