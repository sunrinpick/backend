from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),

    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('articles/page/', views.article_list_page, name='article-list'),
    path('articles/create/', views.article_create_page, name='article-create'),
        path('boards/', views.board_list),
    path('boards/<int:board_pk>/', views.board_detail),
    path('boards/<int:board_pk>/articles/', views.create_article_in_board),
    path('boards/page/', views.board_list_page, name='board-list-page'),
    path('boards/create/', views.board_create_page, name='board-create-page'),
    path('boards/<int:board_pk>/articles/', views.create_article_in_board),
    path('boards/<int:board_pk>/articles/list/', views.list_articles_in_board),
    path('boards/<int:board_pk>/articles/create/', views.board_article_create_page, name='board-article-create-page'),
    path('boards/<int:board_pk>/page/', views.board_detail_page, name='board-detail-page'),
]   
    
    