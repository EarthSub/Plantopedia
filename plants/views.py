from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from plants.models import Plant, PlantCategory

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    plants = Plant.objects.select_related("category")[:6]

    context = {
        "plants": plants,
        "plant_count": Plant.objects.count(),
        "category_count": PlantCategory.objects.count(),
    }

    return render(request,"plants/home.html", context)


def plant_list(request: HttpRequest) -> HttpResponse:
    plants = Plant.objects.select_related("category")
    category_id = request.GET.get("category", "")
    sort_order = request.GET.get("sort", "name")

    if category_id.isdigit():
        plants = plants.filter(category_id=category_id)
    if sort_order in {"name", "-name", "watering_days", "-created_at"}:
        plants = plants.order_by(sort_order)


    context = {
        "plants": plants,
        "categories": PlantCategory.objects.all(),
        "selected_category": category_id,
        "sort_order": sort_order,
    }

    return render(request, "plants/plant_list.html", context)


def plant_detail(request:HttpRequest, pk: int) -> HttpResponse:
    plant = get_object_or_404(
        Plant.objects.select_related("category"),
        pk=pk,
    )

    context = {
        "plant": plant,
    }

    return render(request, "plants/plant_detail.html", context)
