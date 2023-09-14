from django.urls import path
from .views import CategoryListView, PostListView, PostRetrieveView

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path("posts/<str:pk>/", PostRetrieveView.as_view()),
    path("categories/", CategoryListView.as_view()),
]