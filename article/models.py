from django.db import models
from django.urls import reverse
# Create your models here.


class Article(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    time = models.DateTimeField(auto_now_add=True, auto_created=True)
    Context = models.TextField(max_length=10000, blank=False)
    WriterName = models.CharField(max_length=40, blank=False)

    def get_absolute_url(self):
        return reverse("article:ArticleDetail", kwargs={"id": self.id})

    def get_home_url(self):
        return reverse("article:ArticleHome")

    def get_dyn_del_url(self):
        return reverse("article:ArticleDelete", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("article:ArticleEdit", kwargs={"id": self.id})
