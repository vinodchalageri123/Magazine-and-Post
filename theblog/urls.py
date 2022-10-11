from django.urls import path, include
from .import views
from django.contrib import admin
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView, \
    AddCommentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_display', HomeView.as_view(), name="post-display"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name="update-post"),
    path('delete_post/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>/', CategoryView, name="category"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add-comment"),


]
