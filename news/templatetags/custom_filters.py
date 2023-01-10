from django import template


register = template.Library()



@register.filter()
def censor(value):
    censored_value = value.replace('редиска', 'р******').replace('Редиска', 'Р******')
    #b = a.replace('Редиска', 'Р******')

    return censored_value