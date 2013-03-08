from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from rapidsms.router import send
from rapidsms.models import Connection

from dummydata import forms


class GenerateContacts(FormView):
    template_name = 'dummydata/contacts/generate.html'
    form_class = forms.ContactsForm
    success_url = reverse_lazy('generate-contacts')

    def form_valid(self, form):
        form.generate()
        messages.success(self.request, "Contacts generated successfully.")
        return super(GenerateContacts, self).form_valid(form)


class GenerateConnections(FormView):
    template_name = 'dummydata/connections/generate.html'
    form_class = forms.ConnectionsForm
    success_url = reverse_lazy('generate-connections')

    def form_valid(self, form):
        form.generate()
        messages.success(self.request, "Connections generated successfully.")
        return super(GenerateConnections, self).form_valid(form)


class DeleteConnections(FormView):
    template_name = 'dummydata/connections/delete.html'
    form_class = forms.DeleteConnectionsForm
    success_url = reverse_lazy('delete-connections')

    def form_valid(self, form):
        backend = form.cleaned_data['backend']
        Connection.objects.filter(backend=backend).delete()
        messages.success(self.request, "Connections deleted successfully.")
        return super(DeleteConnections, self).form_valid(form)


class SendBulkMessage(FormView):
    template_name = 'dummydata/messages/send_bulk.html'
    form_class = forms.BulkMessageForm
    success_url = reverse_lazy('send-bulk-message')

    def form_valid(self, form):
        send(form.cleaned_data['message'],
             Connection.objects.filter(backend=form.cleaned_data['backend']))
        messages.success(self.request, "Bulk message sent successfully.")
        return super(SendBulkMessage, self).form_valid(form)
