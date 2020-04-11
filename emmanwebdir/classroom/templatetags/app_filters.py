from django import template

register = template.Library()

@register.filter(name='cut_accountnum')
def cut_accountnum(value):
    return ' '.join(('****', '****',str(value)[-4:]))

