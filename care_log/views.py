from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from care_log.forms import CareNoteForm
from care_log.models import CareNote



# Create your views here.


class CareNoteListView(ListView):
    queryset = CareNote.objects.select_related("plant")
    template_name = "care_log/care_note_list.html"
    context_object_name = "notes"


class CareNoteCreateView(SuccessMessageMixin, CreateView):
    model = CareNote
    form_class = CareNoteForm
    template_name = "care_log/care_note_form.html"
    success_url = reverse_lazy("care_note_list")
    success_message = "The care note was added."
    extra_context = {"page_title": "Add a care note"}
