from django import template

register = template.Library()

@register.filter
def currency(value):
    try:
        value = float(value)
        return "R$ {:.2f}".format(value)
    except (ValueError, TypeError):
        return "R$ 0.00"
