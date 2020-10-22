from django.shortcuts import render


def education_view(request):
  return render(request, 'education/education.html', {'education': 'active'})