from django import forms
from django.urls import reverse
from .models import Article


class ArticleModelForm(forms.ModelForm):
    Title = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={"placeholder": "Your Title..."}),
                            label='Title')
    Context = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={"rows": 9,
                                                           "cols": 145,
                                                           "placeholder": "Content..."}),
                              label='Content')
    WriterName = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={"placeholder": "Your Name..."}),
                                 label="Writer's Name")

    class Meta:
        model = Article
        fields = {
            "Title",
            "Context",
            "WriterName"
        }

    def dyn_url_home(self):
        return reverse("article:ArticleHome")

    def clean_Title(self):
        title = self.cleaned_data.get("Title")
        if title[0] == title.lower()[0]:
            raise forms.ValidationError("The First letter should be capital")
        return title
