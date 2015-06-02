import os

import jinja2
import webapp2

from google.appengine.api import taskqueue
from google.appengine.ext import ndb

class persona(ndb.Model):
    nombre = ndb.StringProperty(indexed = True)
    edad = ndb.IntegerProperty(indexed=False)
        
class CounterWorker(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('llego aqui')
        personas = persona.query()
        print(personas)
        for p in personas:
            print(p)
            self.response.out.write(p.nombre)



APP = webapp2.WSGIApplication(
    [
        ('/luciatest', CounterWorker)
    ], debug=True)
