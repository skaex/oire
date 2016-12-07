from django import template
from django.utils.text import slugify
from reports.models import Response

register = template.Library()


@register.simple_tag()
def there_is_report(evaluation, section):
    if evaluation.status != evaluation.STATUSES[2][0]:
        return ''
    response = Response.objects.filter(section=section, evaluation=evaluation)
    if response:
        return '<a href="sections/%s/evaluations/%s/" type="button" class="btn btn-primary btn-xs">%s report</a>' % (
            section.id, evaluation.id, evaluation.name)
    elif evaluation.special:
        return ''
    return '<a href="#" type="button" class="btn btn-default btn-xs disabled">No %s report</a>' % evaluation.name


def get_average_of_response(response):
    total = 0
    total += 1 * response.one
    total += 2 * response.two
    total += 3 * response.three
    total += 4 * response.four
    total += 5 * response.five
    countal = response.one + response.two + response.three + response.four + response.five
    return float(total) / countal


def get_average_of_category(category, responses):
    questions = category.category_questions.all()
    total = 0
    count = 0
    for question in questions:
        for response in responses:
            if question == response.question:
                avg = get_average_of_response(response)
                count += 1
                total += avg
    return total / count


@register.simple_tag()
def response_average(response):
    averg = get_average_of_response(response)

    return "{0:0.2f}".format(averg)


@register.simple_tag()
def category_average(category, responses):
    if responses:
        avg = get_average_of_category(category, responses)
        return "{0:0.2f}".format(avg)
    return None


@register.simple_tag()
def total_average(evaluation, responses):
    if responses:
        total = 0
        count = 0
        categories = evaluation.question_set.category_set.all()
        for category in categories:
            total += get_average_of_category(category, responses)
            count += 1
        return "{0:0.2f}".format(total / count)
    return None


@register.simple_tag()
def total_responses(responses):
    if responses:
        response = responses[0]
        return response.one + response.two + response.three + response.four + response.five
    return None


@register.simple_tag(takes_context=True)
def reports_tabs(context):
    groups = context['request'].user.groups.values_list("name", flat=True)
    # noinspection PyBroadException
    try:
        path_group = context['request'].GET['role']
    except Exception:
        path_group = 'faculty'

    tag = '<ul class="nav nav-tabs">'

    for group in groups:
        if group != 'Administrator':
            tag_class = ''
            if slugify(group) == path_group:
                tag_class = 'active'
            tag += '<li role="presentation" class="%s"><a href="?role=%s">%s</a></li>' % (
                tag_class, slugify(group), group)
    tag += '</ul>'
    return tag
