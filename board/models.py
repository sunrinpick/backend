from django.db import models



class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
# Create your models here.
class Article(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='articles', null=True)  # 추가
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
