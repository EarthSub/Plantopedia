from django.urls import path
from plants import views


urlpatterns = [
    path("", views.plant_list, name="plant_list"),
    path("<int:pk>/", views.plant_detail, name="plant_detail"),

]
