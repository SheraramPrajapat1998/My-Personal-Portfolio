from django.shortcuts import render


def home_view(request):
  context = {
    'home': 'active',
  }
  return render(request, 'core/index.html', context)
