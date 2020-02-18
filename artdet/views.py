from django.shortcuts import render
from articles.models import News
from articles.modelsMore import Categoria


def NoticiaDetail(request, pk):
    # la url debe venir con el pk y luego hacemos fetch con ese pk
    template_path = 'artdet/article_detail.html'
    noticias_qs = News.objects.all()
    noticia = News.object.filter(id=pk)
    context = {'noticias': noticias_qs, 'noticia': noticia}
    return render(request, template_path, context)
