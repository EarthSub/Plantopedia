from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class PlantCategory(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True
    )

    description = models.CharField(
        max_length=240,
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name



class Plant(models.Model):
    name = models.CharField(max_length=90)

    category = models.ForeignKey(
        PlantCategory,
        on_delete=models.PROTECT,
        related_name="plants",
    )

    image = models.ImageField(
        upload_to="plants/",
        null=True,
        blank=True,
    )

    description = models.TextField(max_length=1000)

    watering_days = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(90)
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name", "category"],
                name="plant_name_in_category",
            ),
        ]

    def __str__(self):
        return self.name
