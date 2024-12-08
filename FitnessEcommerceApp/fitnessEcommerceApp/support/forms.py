from django import forms

from fitnessEcommerceApp.support.models import SupportTicket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'message', 'email')
        model = SupportTicket

