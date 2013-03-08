import csv
import urllib
import StringIO
from zipfile import ZipFile

from django import forms

from rapidsms.models import Backend, Contact, Connection


NUMBER_CHOICES = (
    (10, '10'),
    (100, '100'),
    (500, '500'),
    (1000, '1,000'),
    (10000, '10,000'),
)


class ContactsForm(forms.Form):
    "Form to generate lots of contacts."

    number = forms.ChoiceField(choices=NUMBER_CHOICES)
    backend = forms.ModelChoiceField(queryset=Backend.objects.all())

    def generate(self):
        Contact.objects.all().delete()
        url = urllib.urlopen("http://www.opensourcecf.com/randomNames.zip")
        zfile = ZipFile(StringIO.StringIO(url.read()))
        data = StringIO.StringIO(zfile.read("randomNames.csv"))
        reader = csv.reader(data)
        contacts = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            contacts.append(Contact(name=row[3]))
            if i >= int(self.cleaned_data['number']):
                break
        Contact.objects.bulk_create(contacts)
        identity = 1110001111
        connections = []
        for contact in Contact.objects.all():
            connection = Connection(backend=self.cleaned_data['backend'],
                                    identity=identity, contact=contact)
            connections.append(connection)
            identity += 1
        Connection.objects.bulk_create(connections)


class ConnectionsForm(forms.Form):
    "Form to generate lots of connections."

    number = forms.ChoiceField(choices=NUMBER_CHOICES)
    backend = forms.ModelChoiceField(queryset=Backend.objects.all())

    def generate(self):
        Connection.objects.all().delete()
        connections = []
        identity = 2220001111
        for x in xrange(int(self.cleaned_data['number'])):
            connection = Connection(backend=self.cleaned_data['backend'],
                                    identity=identity)
            connections.append(connection)
            identity += 1
        Connection.objects.bulk_create(connections)


class DeleteConnectionsForm(forms.Form):
    "Form to delete connections by backend."

    backend = forms.ModelChoiceField(queryset=Backend.objects.all())


class BulkMessageForm(forms.Form):
    "Form to send a bulk message to all connections of a backend."

    message = forms.CharField()
    backend = forms.ModelChoiceField(queryset=Backend.objects.all())
