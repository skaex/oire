from django import template
from ..models import PreSection

register = template.Library()

@register.simple_tag()
def load_button():
    presections = PreSection.objects.count()
    if  presections == PreSection.objects.filter(error_column="").count() and presections > 0:
        return '<a href="/sections/sections/load/" type="button" class="btn btn-xs btn-primary"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Load to sections</a>'
    elif presections <= 0:
        return '<a href="#" type="button" class="btn btn-xs btn-warning disabled"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> No presections to load</a>'
    else:
        return '<a href="#" type="button" class="btn btn-xs btn-danger disabled"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Some Presections are not ready</a>'
