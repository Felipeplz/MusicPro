from django import template
from musicpro.views.moneda import convertir

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def minus(value, arg):
    return value - arg

@register.filter
def conversion(value, arg):
    return convertir(arg, int(value)) 