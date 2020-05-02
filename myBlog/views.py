from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.

def hello(request):
    return HttpResponse('first time?')


def index(request):
    siteName = 'Simon的Blog'
    description = '记录自己学习'
    url = 'www.simonBlog.com'
    allArticle = Article.objects.all()
    context = {
        'siteName': siteName,
        'url': url,
        'description': description,
        'allArticle': allArticle,
    }
    return render(request, 'index.html', context)
