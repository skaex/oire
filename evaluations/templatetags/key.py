from django import template
from evaluations.models import Key

register = template.Library()

@register.simple_tag()
def keyslabelclass(status):
	statuses = Key.KEY_STATUSES
	if (status == statuses[0][0]):
		return 'label-success'
	elif (status == statuses[1][0]):
		return 'label-warning'
	elif (status == statuses[2][0]):
		return 'label-danger'
	else:
		return 'label-default'