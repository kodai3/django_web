from django import template

register = template.Library()

@register.filter(name='mycut')
def mycut(value, arg):
    """
    this cut sou al values of 'arg' from the string
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
