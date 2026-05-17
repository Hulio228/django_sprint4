from django.http import HttpResponse
from django.shortcuts import render


def about(request) -> HttpResponse:
    template: str = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    template: str = 'pages/rules.html'
    return render(request, template)
