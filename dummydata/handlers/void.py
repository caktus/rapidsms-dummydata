from rapidsms.contrib.handlers.handlers.base import BaseHandler


class VoidHandler(BaseHandler):

    @classmethod
    def dispatch(cls, router, msg):
        if msg.text == "void":
            return True
