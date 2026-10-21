from django import forms
from plant_collections.models import PlantCollection


class PlantCollectionForm(forms.ModelForm):
    class Meta:
        model = PlantCollection
        fields = ["title", "description", "plants"]
        labels = {
            "title": "Collection name",
            "description": "Description",
            "plants": "Plants in this collection",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "For example, Desk plants"}),
            "description": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Describe the collection."}
            ),
            "plants": forms.CheckboxSelectMultiple,
        }
        error_messages = {
            "title": {"required": "Enter a name for the collection."},
        }
