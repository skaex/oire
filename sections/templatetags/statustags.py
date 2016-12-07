from django import template
from sections.models import Section
from evaluations.models import Evaluation

register = template.Library()


@register.simple_tag()
def status(status, semester, section):
    open_evaluation = Evaluation.objects.filter(semester=semester).filter(status=Evaluation.STATUSES[0][0])
    section_statuses = Section.STATUSES
    if (status == section_statuses[0][1]):
        return '<a href="/sections/section/close/%s/" type="button" class="btn btn-xs btn-success">%s</a>' % (
        section, status)
    elif (status == section_statuses[1][1]):
        if (open_evaluation):
            return '<a href="/sections/section/open/%s/" type="button" class="btn btn-xs btn-primary">%s</a>' % (
            section, status)
        return '<a href="#" type="button" class="btn btn-xs btn-danger disabled">%s</a>' % (status)
    elif (status == section_statuses[2][1]):
        return '<a href="/sections/section/close/%s/" type="button" class="btn btn-xs btn-info">%s</a>' % (
        section, status)
    elif (status == section_statuses[3][1]):
        return '<a href="#" type="button" class="btn btn-xs btn-default disabled">%s</a>' % (status)
    else:
        return ''
