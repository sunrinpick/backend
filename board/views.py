from django.urls import is_valid_path
from board.serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from .forms import BoardForm  
from .models import Board

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Board
from .serializers import BoardSerializer

from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)





@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



def article_list_page(request):
    articles = Article.objects.all().order_by('-pk')
    return render(request, 'articles/board_list.html', {'articles': articles})

def article_create_page(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
    else:
        form = ArticleForm()
    return render(request, 'articles/board_form.html', {'form': form})


@api_view(['GET', 'POST'])
def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_article_in_board(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    




# 게시판 목록 페이지
def board_list_page(request):
    boards = Board.objects.all().order_by('-pk')
    return render(request, 'boards/boards_list.html', {'boards': boards})

# 게시판 생성 페이지
def board_create_page(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board-list-page')
    else:
        form = BoardForm()
    return render(request, 'boards/boards_form.html', {'form': form})


@api_view(['POST'])
def create_article_in_board(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET'])
def list_articles_in_board(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    articles = board.articles.all()  # related_name='articles' 덕분에 가능
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


def board_article_create_page(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.board = board
            article.save()
            return redirect('board-list-page')  # 혹은 게시글 목록으로 redirect
    else:
        form = ArticleForm()
    
    return render(request, 'boards/board_article_form.html', {
        'form': form,
        'board': board,
    })

def board_detail_page(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    articles = board.articles.all().order_by('-pk')  # related_name='articles' 덕분

    return render(request, 'boards/board_detail.html', {
        'board': board,
        'articles': articles,
    })