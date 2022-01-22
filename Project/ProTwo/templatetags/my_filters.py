from django import template

register = template.Library()

def cut_filter(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

register.filter('cut', cut_filter)
# 1st para : name the filter
# 2nd para : name of function