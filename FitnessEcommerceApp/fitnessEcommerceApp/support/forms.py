from django import forms

from fitnessEcommerceApp.support.models import SupportTicket


class CreateTicketForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'message', 'email')
        model = SupportTicket

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'title':
                field.widget.attrs = {'placeholder': 'Enter the title of the problem...'}

            if field_name == 'message':
                field.widget.attrs = {'placeholder': 'Explain what the problem is...'}

            if field_name == 'email':
                field.widget.attrs = {'placeholder': 'Enter a valid email...'}
