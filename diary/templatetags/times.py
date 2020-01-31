from django import template
register = template.Library()

@register.filter(name="times")
def times(rng):
    return range(1, rng + 1, 1)
