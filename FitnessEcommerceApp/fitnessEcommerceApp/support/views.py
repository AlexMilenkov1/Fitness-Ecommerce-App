from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from fitnessEcommerceApp.support.forms import CreateTicketForm


class AddTicket(LoginRequiredMixin, CreateView):
    template_name = 'tickets.html'
    form_class = CreateTicketForm

    def form_valid(self, form):
        ticket = form.save(commit=False)

        ticket.user = self.request.user

        ticket.save()

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path_info
