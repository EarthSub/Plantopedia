from django.shortcuts import render
from care_log.models import CareNote
from django.views import View


# Create your views here.


class CareNoteListView(View):
    template_name = "care_log/care_note_list.html"

    def get(self, request):
        notes = CareNote.objects.select_related("plant")
        context = {"notes": notes}
        return render(request, self.template_name, context)
