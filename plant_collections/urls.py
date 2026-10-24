from django.urls import path
from plant_collections import views

urlpatterns = [
    path("", views.CollectionListView.as_view(), name="collection_list"),
    path("<int:pk>/", views.CollectionDetailView.as_view(), name="collection_detail"),
    path("new/", views.CollectionCreateView.as_view(), name="collection_create"),
    path("<int:pk>/edit/", views.CollectionUpdateView.as_view(), name="collection_update"),
    path("<int:pk>/delete/", views.CollectionDeleteView.as_view(), name="collection_delete"),
]
