from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'is_published', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
