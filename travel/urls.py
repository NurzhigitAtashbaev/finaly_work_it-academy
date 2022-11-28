from django.urls import path, include
from .views import (TourListView, TourDetailView, CategoryDetailView, TypesDetailView,
                    CreateTourViews, EntryTourViews)

urlpatterns = [
    path('all/', TourListView.as_view()),
    path('detail/<int:pk>/', TourDetailView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('types/<int:pk>/', TypesDetailView.as_view()),

    path('create/', CreateTourViews.as_view()),
    path('entry/', EntryTourViews.as_view()),

]