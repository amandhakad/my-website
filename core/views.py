from django.shortcuts import render

from django.http import HttpResponse

from .models import Post
from django.views import generic


def index(request):
    return render(request, 'core/index.html')

class PostsView(generic.ListView):
	template_name = 'core/posts_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(status='1')

class SinglePostView(generic.DetailView):
	model = Post