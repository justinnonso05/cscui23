from django.urls import path
from . import views
from .views import HomeView, CreatePostView, PostDetailView, PhotoView, SearchResultView, UpdatePostView, DeletePostView



urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('new-post/', CreatePostView.as_view(), name = 'create-post'),
    path('posts/<int:pk>/<str:username>/', PostDetailView.as_view(), name = 'post-detail'),
    path('posts/edit/<int:pk>/', UpdatePostView.as_view(), name = 'edit-post'),
    path('posts/delete/<int:pk>/', DeletePostView.as_view(), name = 'delete-post'),
    path('app/photos/', PhotoView.as_view(), name = 'photos'),
    path('app/search/', SearchResultView.as_view(), name = 'search'),
    path('app/level_materials/', views.materials, name = 'materials'),
    path('app/calendar/', views.calendar, name = 'calendar'),
    path('announcements/', views.announcement, name = 'announcement'),
    path('like/<int:post_id>/', views.like_post, name = 'like-post'),
]