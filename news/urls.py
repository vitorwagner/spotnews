from django.urls import path
from news.views import home, news_details, category, news_form

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", category, name="categories-form"),
    path("news/", news_form, name="news-form"),
]
