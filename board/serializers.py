from rest_framework import serializers
from .models import Article, Comment
from .models import Board

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        


class BoardSerializer(serializers.ModelSerializer):
    articles = ArticleListSerializer(many=True, read_only=True)  # related_name='articles' 덕분에 가능

    class Meta:
        model = Board
        fields = '__all__'