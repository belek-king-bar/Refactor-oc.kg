from django import template

register = template.Library()


@register.filter
def get_hours(seconds):
    return seconds // 3600


@register.filter
def get_minutes(seconds):
    return (seconds % 3600) // 60