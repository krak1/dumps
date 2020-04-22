from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = "home.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "dynView.html"
    # queryset = Article.objects.all() => This is not necessary

    def get_object(self, queryset=None):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Article, id=my_id)


class ArticleCreateView(CreateView):
    template_name = "create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = "/"                 (or)
    # def get_success_url(self):
    #    return                         (or) default is from 'get_absolute_url' in .models


class ArticleUpdateView(UpdateView):
    template_name = "create.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self, queryset=None):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Article, id=my_id)


class ArticleDeleteView(DeleteView):
    template_name = "delConf.html"

    def get_object(self, queryset=None):
        my_id = self.kwargs.get("id")
        return get_object_or_404(Article, id=my_id)

    def get_success_url(self):
        return reverse("article:ArticleHome")
