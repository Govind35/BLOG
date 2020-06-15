from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView


urlpatterns = [
    path('',PostListView.as_view(), name= 'blog-home'),     # name is used in html page to link the url  
    path('post/new/',PostCreateView.as_view(), name= 'post-create'),      
    path('post/<int:pk>/',PostDetailView.as_view(), name= 'post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name= 'post-update'),
    path('about/',views.about, name= 'blog-about')
]

