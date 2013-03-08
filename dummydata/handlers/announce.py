from rapidsms.router import send

from rapidsms.models import Connection

from rapidsms.contrib.handlers.handlers.pattern import PatternHandler


class AnnounceHandler(PatternHandler):
    pattern = r'^announce ([\w-]+) (\w+)$'

    def handle(self, backend_name, text):
        connections = Connection.objects.filter(backend__name=backend_name)
        send(text, connections)
