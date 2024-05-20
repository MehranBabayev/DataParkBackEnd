from django.urls import path
from .views import (
    BlogListAPIView,
    BlogCommentAPIView,
    BlogCommentUpdateAPIView,
    BlogDetailView,
    BlogUpdateView,
    LikeDislikeCreateView
)

urlpatterns = [
    path('', BlogListAPIView.as_view(), name='blogs'),
    path('comments/', BlogCommentAPIView.as_view(), name='blog_comment_list'),
    path('comment/<int:pk>/',BlogCommentUpdateAPIView.as_view(), name='blog_comment_update'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('comments/like-dislike/', LikeDislikeCreateView.as_view(), name='like-dislike-comment')
]