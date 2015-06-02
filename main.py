import os

import webapp2

from google.appengine.ext import ndb
from google.appengine.api import mail
from datetime import datetime

class NotifConfig(ndb.Model):
    notification_type = ndb.StringProperty()
    notification_date = ndb.DateProperty()
     
class DataRetriever(webapp2.RequestHandler):
    def get(self):
        #if self.request.headers.get('X-AppEngine-Cron'):
            today = datetime.today().replace(hour=00,minute=00,second=00,microsecond=0)
            notifications = NotifConfig.query(NotifConfig.notification_date == today)
            print notifications
            for n in notifications:
                mail.send_mail(sender="Lucia analucia0189@gmail.com",
                    to="analucia0189@gmail.com",
                    subject="Email notif",
                    body="Hoy es dia de notificacion!!!")



APP = webapp2.WSGIApplication(
    [
        ('/retrievedata', DataRetriever)
    ])
