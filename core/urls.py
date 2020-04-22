from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', views.SinglePostView.as_view(), name='Post')
]