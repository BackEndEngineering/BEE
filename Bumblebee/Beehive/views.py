from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    recent_articles = Article.objects.order_by('-publish_date')[:10]
    context = {'recent_articles': recent_articles}
    return render(request, 'Beehive/articles.html', context)

def view_article(request, article_id):

    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("No such article!")

    return render(request, 'Beehive/article.html')
