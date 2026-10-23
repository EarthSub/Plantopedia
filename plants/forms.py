from django import forms
from plants.models import Plant, PlantCategory


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = [
            "name",
            "category",
            "image",
            "description",
            "watering_days",
        ]
        labels = {
            "name": "Common name",
            "category": "Category",
            "description": "Description",
            "watering_days": "Water every (days)",
        }
        help_texts = {
            "watering_days": "Choose a number from 1 to 90.",
        }
        error_messages = {
            "name": {"required": "Enter a name for this plant."},
            "description": {"required": "Add a short description."},
            "watering_days": {
                "min_value": "Choose an interval of at least 1 day.",
                "max_value": "Choose an interval of no more than 90 days.",
            },
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "For example, Monstera"}),
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe this plant."}
            ),
            "watering_days": forms.NumberInput(attrs={"min": 1, "max": 90}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("The name must contain at least two characters.")
        return name


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        category = cleaned_data.get("category")

        if name and category:
            duplicates = Plant.objects.filter(name__iexact=name, category=category)
            if self.instance.pk:
                duplicates = duplicates.exclude(pk=self.instance.pk)
            if duplicates.exists():
                self.add_error("name", "A plant with this name is already in this category.")

        return cleaned_data


class PlantCategoryForm(forms.ModelForm):
    class Meta:
        model = PlantCategory
        fields = ["name", "description"]
        labels = {"name": "Category name", "description": "Description"}
        error_messages = {
            "name": {"required": "Enter a name for this category."},
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "For example, Herbs"}),
            "description": forms.TextInput(
                attrs={"placeholder": "What plants belong here?"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if PlantCategory.objects.filter(name__iexact=name).exclude(
            pk=self.instance.pk
        ).exists():
            raise forms.ValidationError("A category with this name already exists.")
        return name