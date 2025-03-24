from django import template
from ..models import Department

register = template.Library()

@register.filter(name='is_department')       # This filter checks if the given object is an instance of the Department model.
def is_department(obj):
    return isinstance(obj, Department)