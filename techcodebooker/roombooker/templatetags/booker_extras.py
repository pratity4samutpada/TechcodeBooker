from django import template
from ..models import Bookings
from django import forms
register = template.Library()

class ApproveBooking(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['status']
        widgets = {
            'status':forms.HiddenInput()
        }



@register.inclusion_tag('tagtemplates/pending.html')
def pending_bookings():
    pending = Bookings.objects.filter(status=True)
    pending_b = []
    for booking in pending:
        obj={}
        obj['form'] = ApproveBooking(instance=booking,initial={'status':False})
        obj['info'] = booking
        pending_b.append(obj)
    return {'pending': pending_b}


