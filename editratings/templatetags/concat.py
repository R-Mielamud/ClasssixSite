from django import template
register = template.Library()

@register.filter(name="concat")
def concat(str1, str2):
    return str(str1) + str(str2)
