from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /posts/5/
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('posts/edit/<int:post_id>/', views.post_edit, name='edit'),
    path('posts/new',views.post_new,name="new_post")
]