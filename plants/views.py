from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView, ListView, CreateView
from plants.forms import PlantForm, PlantCategoryForm
from plants.models import Plant, PlantCategory


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


class PlantDetailView(DetailView):
    model = Plant
    queryset = Plant.objects.select_related("category")
    template_name = "plants/plant_detail.html"
    context_object_name = "plant"


def plant_create(request: HttpRequest) -> HttpResponse:
    form = PlantForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        plant = form.save()
        messages.success(request, f"{plant.name} was added to the catalogue.")
        return redirect("plant_detail", pk=plant.pk)

    context = {
        "form": form,
        "page_title": "Add a plant",
    }

    return render(request, "plants/plant_form.html", context)


def plant_update(request:HttpRequest, pk) -> HttpResponse:
    plant = get_object_or_404(Plant, pk=pk)
    form = PlantForm(request.POST or None, request.FILES or None, instance=plant)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "The plant details were updated.")
        return redirect("plant_detail", pk=plant.pk)

    context = {
        "form": form,
        "page_title": "Update a plant"
    }

    return render(request, "plants/plant_form.html", context)


class PlantDeleteView(DeleteView):
    model = Plant
    template_name = "plants/plant_confirm_delete.html"
    context_object_name = "plant"
    success_url = reverse_lazy("plant_list")

    def form_valid(self, form):
        messages.success(self.request, "The plant was deleted.")
        return super().form_valid(form)


class CategoryListView(ListView):
    model = PlantCategory
    template_name = "plants/category_list.html"
    context_object_name = "categories"


def category_detail(request: HttpRequest, pk) -> HttpResponse:
    category = get_object_or_404(PlantCategory, pk=pk)
    plants = category.plants.select_related("category")

    context = {
        "category": category,
        "plants": plants,
    }

    return render(request, "plants/category_detail.html", context)


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = PlantCategory
    form_class = PlantCategoryForm
    template_name = "plants/category_form.html"
    success_message = "The category was created."
    extra_context = {"page_title": "Add a category"}

    def get_success_url(self):
        return reverse("category_detail", kwargs={"pk": self.object.pk})


def page_not_found(request: HttpRequest, unmatched_path=None) -> HttpResponse:
    return render(request, "404.html", status=404)
