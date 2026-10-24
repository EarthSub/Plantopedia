from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from plant_collections.forms import PlantCollectionForm
from plant_collections.models import PlantCollection


# Create your views here.


class CollectionListView(ListView):
    queryset = PlantCollection.objects.prefetch_related("plants")
    template_name = "plant_collections/collection_list.html"
    context_object_name = "collections"


class CollectionDetailView(DetailView):
    model = PlantCollection
    queryset = PlantCollection.objects.prefetch_related("plants")
    template_name = "plant_collections/collection_detail.html"
    context_object_name = "collection"


class CollectionCreateView(SuccessMessageMixin, CreateView):
    model = PlantCollection
    form_class = PlantCollectionForm
    template_name = "plant_collections/collection_form.html"
    success_message = "The collection was created."
    extra_context = {"page_title": "Add a collection"}

    def get_success_url(self):
        return reverse("collection_detail", kwargs={"pk": self.object.pk})


class CollectionUpdateView(SuccessMessageMixin, UpdateView):
    model = PlantCollection
    form_class = PlantCollectionForm
    template_name = "plant_collections/collection_form.html"
    success_message = "The collection was updated."
    extra_context = {"page_title": "Edit collection"}

    def get_success_url(self):
        return reverse("collection_detail", kwargs={"pk": self.object.pk})


class CollectionDeleteView(DeleteView):
    model = PlantCollection
    template_name = "plant_collections/collection_confirm_delete.html"
    context_object_name = "collection"
    success_url = reverse_lazy("collection_list")

    def form_valid(self, form):
        messages.success(self.request, "The collection was deleted.")
        return super().form_valid(form)
