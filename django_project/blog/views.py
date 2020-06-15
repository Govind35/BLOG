from django.shortcuts import render
from django.http import HttpResponse # for using Httpresponse
from django.contrib.auth.mixins import LoginRequiredMixin   # class cant use loginRequired decorater so LoginRequiredMixin is used
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post # for getting data from Post database


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # naming covention is appname/model_viewtype.html for ListView but we can change it here
    context_object_name = 'posts'       # to tell listview  which object to be passed which we used in html file 
    ordering = ['-date_posted']

class PostDetailView(DetailView):       # naming covention is appname/model_viewtype.html for DetailView
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):       # naming covention is appname/model_viewtype.html for CreateView
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):     # to set logged in user for post
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):       # naming covention is appname/model_viewtype.html for CreateView
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):     # to set logged in user for post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})   


