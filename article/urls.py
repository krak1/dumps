from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = "article"
urlpatterns = [
    path('', ArticleListView.as_view(), name="ArticleHome"),
    path('<int:id>/', ArticleDetailView.as_view(), name="ArticleDetail"),
    path('create/', ArticleCreateView.as_view(), name="ArticleCreate"),
    path('<int:id>/edit', ArticleUpdateView.as_view(), name="ArticleEdit"),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name="ArticleDelete"),

    ]
