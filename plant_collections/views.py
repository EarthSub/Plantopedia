from django.shortcuts import render, get_object_or_404
from django.views import View
from plant_collections.models import PlantCollection


# Create your views here.


class CollectionListView(View):
    template_name = "plant_collections/collection_list.html"

    def get(self, request):
        collections = PlantCollection.objects.prefetch_related("plants")
        context = {"collections": collections}
        return render(request, self.template_name, context)


class CollectionDetailView(View):
    template_name = "plant_collections/collection_detail.html"

    def get(self, request, pk):
        collection = get_object_or_404(
            PlantCollection.objects.prefetch_related("plants"),
            pk=pk,
        )
        context = {"collection": collection}
        return render(request, self.template_name, context)

