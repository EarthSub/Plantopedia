from django.urls import path
from plant_collections import views

urlpatterns = [
    path("", views.CollectionListView.as_view(), name="collection_list"),
    path("<int:pk>/", views.CollectionDetailView.as_view(), name="collection_detail"),

]
