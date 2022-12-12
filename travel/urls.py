from django.urls import path
from .views import (TourListView, TourDetailView,
                    CategoryDetailView, TypesDetailView,
                    CreateTourViews, EntryTourViews,
                    CreateCommentView, DeleteCommentView, LikeCreateView, LikeDeleteView)

urlpatterns = [
    path('create/', CreateTourViews.as_view(), name='tour-create'),
    path('all/', TourListView.as_view(), name='tour-list'),
    path('detail/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),

    path('category/<int:pk>/', CategoryDetailView.as_view(), name='tour-category'),
    path('types/<int:pk>/', TypesDetailView.as_view(), name='tour-types'),
    path('entry/', EntryTourViews.as_view(), name='tour-entry'),

    path('comment/', CreateCommentView.as_view(), name='tour-comments'),
    path('delete_comment/<int:pk>/', DeleteCommentView.as_view(), name='comments-delete'),
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('like_delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),

]
