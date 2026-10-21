from django import forms
from care_log.models import CareNote


class CareNoteForm(forms.ModelForm):
    class Meta:
        model = CareNote
        fields = ["plant", "title", "note"]
        labels = {
            "plant": "Plant",
            "title": "Title",
            "note": "Care note",
        }
        error_messages = {
            "plant": {"required": "Choose a plant."},
            "title": {"required": "Enter a title."},
            "note": {"required": "Write a short caer note."},
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "For example, New leaf"}),
            "note": forms.Textarea(
                attrs={"rows": 4, "placeholder": "What did you do or notice?"}
            ),
        }
