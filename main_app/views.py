from django.shortcuts import render

finches = [
  {'name': 'Ruby', 'breed': 'Gouldian', 'description': 'calm demeanor and enjoys bathing in a shallow dish', 'age': 1},
  {'name': 'Sunny', 'breed': 'Zebra', 'description': 'cheerful and active personality', 'age': 2},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })