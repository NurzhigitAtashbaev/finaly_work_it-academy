from django.urls import path
from .views import (TourListView, TourDetailView,
                    CategoryDetailView, TypesDetailView,
                    CreateTourViews, EntryTourViews,
                    CreateCommentView, DeleteCommentView,)


urlpatterns = [
    path('all/', TourListView.as_view(),name='tour-list'),
    path('detail/<int:pk>/', TourDetailView.as_view(),name='tour-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(),name='category-detail'),
    path('types/<int:pk>/', TypesDetailView.as_view(),name='tour-types'),
    path('create/', CreateTourViews.as_view(),name='tour-create'),
    path('entry/', EntryTourViews.as_view(),name='tour-entry'),
    path('comment/', CreateCommentView.as_view(),name='tour-comments'),
    path('delete_comment/<int:pk>/', DeleteCommentView.as_view(),name='delete-comment'),
]