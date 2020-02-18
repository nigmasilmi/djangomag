from django.shortcuts import render
from articles.models import News
from publicidade.models import Publicidad


def home(request):
    template_path = 'pages/index.html'
    news_qs = News.objects.all()
    latest_qs = news_qs.order_by('-created_at')[:3]
    pub_qs = Publicidad.objects.all()
    context = {'news': news_qs, 'latest': latest_qs, 'publi': pub_qs}
    return render(request, template_path, context)


def archive(request):
    template_path = 'pages/archive.html'
    news_qs = News.objects().all
    context = {'news': news_qs}
    return render(request, template_path, context)


def category(request):
    template_path = 'pages/category.html'
    context = {}
    return render(request, template_path, context)


def aboutUs(request):
    template_path = 'pages/aboutUs.html'
    context = {}
    return render(request, template_path, context)


def contact(request):
    template_path = 'pages/contact.html'
    context = {}
    return render(request, template_path, context)


def standard_post(request):
    template_path = 'pages/standard-post.html'
    context = {}
    return render(request, template_path, context)
