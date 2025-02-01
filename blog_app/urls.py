from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home_view, name='home_view'),  # Home page displaying blog feed
    path('blog/create/', views.create_blog, name='create_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('<int:blog_id>/like/', views.like_blog, name='like_blog'),
    path('comment/create/<int:blog_id>/', views.create_comment, name='create_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
