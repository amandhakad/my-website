from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Post
from django.views import generic


def index(request):
    return render(request, 'core/index.html')

class PostsView(generic.ListView):
	template_name = 'core/posts_list.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.all()
