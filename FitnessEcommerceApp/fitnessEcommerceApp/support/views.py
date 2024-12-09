from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView

from fitnessEcommerceApp.support.forms import CreateTicketForm
from fitnessEcommerceApp.support.models import SupportTicket


class AddTicket(LoginRequiredMixin, CreateView):
    template_name = 'tickets/add-ticket.html'
    form_class = CreateTicketForm

    def form_valid(self, form):
        ticket = form.save(commit=False)

        ticket.user = self.request.user

        ticket.save()

        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path_info


class TicketsForReview(LoginRequiredMixin, PermissionRequiredMixin,  ListView):
    template_name = 'tickets/ticket-review.html'
    context_object_name = 'tickets'
    model = SupportTicket
    permission_required = 'support.can_resolve_tickets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tickets_to_resolve_count = 0
        all_tickets = SupportTicket.objects.all()

        for ticket in all_tickets:
            if not ticket.is_resolved:
                tickets_to_resolve_count += 1

        context['tickets_to_resolve_count'] = tickets_to_resolve_count

        return context


@permission_required('support.can_resolve_tickets')
def resolve_ticket(request, pk):
    ticket = SupportTicket.objects.get(pk=pk)

    ticket.is_resolved = True

    ticket.save()

    return redirect('review-tickets')
