from blog import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('weekly/<int:pk>/', views.detail, name='blog_detail'),
    path('blog/create/', views.create_blog, name = 'blog_create'),
    path('blog/drafts/', views.draft_blogs, name='blog_drafts'),
    path('weekly/<int:blog_id>/update/', views.update_blog, name='blog_update'),
    path('blog/<int:pk>/publish/', views.blog_publish, name='blog_publish'),
    path('blog/<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('comment/<int:pk>/remove/',views.comment_remove, name='comment_remove'),

]
