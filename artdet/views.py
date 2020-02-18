from django.shortcuts import render, get_object_or_404
from articles.models import News
from articles.modelsMore import Categoria


def NoticiaDetail(request, noticia_id):
    # la url debe venir con el pk y luego hacemos fetch con ese pk
    template_path = 'artdet/article_detail.html'
    # noticias_qs = News.objects.all()
    # noticia = News.objects.filter(id=noticia_id)
    noticia = get_object_or_404(News, pk=noticia_id)
    context = {'noticia': noticia}
    return render(request, template_path, context)
