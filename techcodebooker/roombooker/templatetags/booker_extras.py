from django import template
from ..models import Bookings

register = template.Library()

@register.inclusion_tag('tagtemplates/pending.html')
def pending_bookings():
    pending = Bookings.objects.filter(status=True)
    return {'pending': pending}
