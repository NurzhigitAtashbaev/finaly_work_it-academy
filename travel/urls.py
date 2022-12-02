from django.urls import path
from .views import (TourListView, TourDetailView, CategoryDetailView, TypesDetailView,
                    CreateTourViews, EntryTourViews, CreateCommentView, DeleteCommentView)

urlpatterns = [
    path('all/', TourListView.as_view()),
    path('detail/<int:pk>/', TourDetailView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('types/<int:pk>/', TypesDetailView.as_view()),

    path('create/', CreateTourViews.as_view()),
    path('entry/', EntryTourViews.as_view()),
    path('comment/', CreateCommentView.as_view()),
    path('delete_comment/<int:pk>/', DeleteCommentView.as_view()),

]
