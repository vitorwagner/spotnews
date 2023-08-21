from django.urls import path, include
from news.views import home, news_details, category, news_form
from rest_framework import routers
from news_rest.views.categories_view import CategoriesViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoriesViewSet)

urlpatterns = [
    path("", home, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
    path("categories/", category, name="categories-form"),
    path("news/", news_form, name="news-form"),
    path("api/", include(router.urls)),
]
