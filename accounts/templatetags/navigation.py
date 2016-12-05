from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    pattern = pattern_or_urlname
    path = context['request'].path.split('/')[-2]
    if (pattern == path):
        return 'active'
    return ''