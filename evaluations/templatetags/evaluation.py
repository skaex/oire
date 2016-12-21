from django import template
from evaluations.models import Evaluation
from sections.models import Section

register = template.Library()


@register.simple_tag()
def statuslink(status, evaluation):
    evaluation_statuses = Evaluation.STATUSES
    open_evaluation = Evaluation.objects.filter(status=evaluation_statuses[0][0])
    if status == evaluation_statuses[0][0]:
        return '<a href="/evaluations/evaluation/finish/%s/" type="button" class="btn btn-info btn-xs">%s</a>' % (
            evaluation, evaluation_statuses[0][1])
    elif status == evaluation_statuses[1][0] and not open_evaluation:
        return '<a href="/evaluations/evaluation/open/%s/" type="button" class="btn btn-danger btn-xs">%s</a>' % (
            evaluation, evaluation_statuses[1][1])
    elif status == evaluation_statuses[2][0]:
        return '<a href="#" type="button" class="btn btn-success btn-xs disabled">%s</a>' % (evaluation_statuses[2][1])
    else:
        return ''


@register.simple_tag()
def open_all_sections_link(evaluation):
    if evaluation.status == evaluation.STATUSES[0][0]:
        return '<a href="/evaluations/evaluation/%s/sections/open/" \
        type="button" class="btn btn-info btn-xs">Open all section(s)  <span class="badge">%s</span></a>' % (
            evaluation.id, evaluation.semester.section_set.filter(status=Section.STATUSES[1][0]).count())
    return ''
