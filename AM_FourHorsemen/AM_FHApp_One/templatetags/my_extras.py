from django import template


register = template.Library()

def cut1(value,arg):
    # This cuts out all values of arg from string!

    return value.replace(arg,'')

register.filter('cut1',cut1)
# First is string used in template tag, after comma it is the function name
