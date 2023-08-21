from django.shortcuts import render
from news.models import News


def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)


def news_details(request, id):
    news = News.objects.get(id=id)
    context = {"news": news}
    return render(request, "news_details.html", context)
