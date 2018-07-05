from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from catalog.models import Article


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    return HttpResponse(render(request, 'index.html', {
        'articles': articles
    }))
