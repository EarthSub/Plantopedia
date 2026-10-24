from django.urls import path
from plants import views


urlpatterns = [
    path("", views.plant_list, name="plant_list"),
    path("<int:pk>/", views.PlantDetailView.as_view(), name="plant_detail"),
    path("new/", views.plant_create, name="plant_create"),
    path("<int:pk>/edit/", views.plant_update, name="plant_update"),
    path("<int:pk>/delete/", views.PlantDeleteView.as_view(), name="plant_delete"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/new/", views.CategoryCreateView.as_view(), name="category_create"),
    path("categories/<int:pk>/", views.category_detail, name="category_detail"),
]
