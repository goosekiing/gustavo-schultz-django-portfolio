from django import template
from portfolio.views import DEFAULT_QUERIES

register = template.Library()

@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    request = context['request']
    updated = request.GET.copy()

    for k, v in kwargs.items():
        default_value = DEFAULT_QUERIES.get(k)
        if v is not None and v != "None" and v != default_value:
            updated[k] = v
        elif k in updated:
            del updated[k]
    
    return updated.urlencode()
