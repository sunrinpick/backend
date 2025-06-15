from django import forms
from .models import Article
from .models import Board

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description']
