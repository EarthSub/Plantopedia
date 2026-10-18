from django.db import models
from plants.models import Plant



class PlantCollection(models.Model):
    title = models.CharField(max_length=50)

    description = models.CharField(
        max_length=240,
        blank=True
    )

    plants = models.ManyToManyField(
        Plant,
        related_name="collections",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title