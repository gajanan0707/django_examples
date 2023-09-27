from django.shortcuts import render


def index(request):
    context = {'name': 'GreekForGreek'}  # Example context data
    return render(request, 'jinja_example.html', context)