from django import template

register = template.Library()


@register.filter
def watering_schedule(days):
    return f"Every {days} days" if days else "No schedule set"


@register.simple_tag
def category_plant_count(category):
    return category.plants.count()
