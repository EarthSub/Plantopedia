from django.urls import path
from care_log import views


urlpatterns = [
    path("", views.CareNoteListView.as_view(), name="care_note_list"),
]
