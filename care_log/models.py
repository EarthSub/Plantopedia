from django.db import models
from plants.models import Plant



class CareNote(models.Model):
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        related_name="care_notes",
    )

    title = models.CharField(max_length=90)

    note = models.TextField(max_length=900)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.plant.name}: {self.title}"