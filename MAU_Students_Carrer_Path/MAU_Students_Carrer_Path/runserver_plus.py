from django.core.management.commands.runserver import Command as RunserverCommand
from django.conf import settings
from django.conf.urls.static import static
from django.core.wsgi import get_wsgi_application
from django.core.servers.basehttp import run
import sys
import os

class Command(RunserverCommand):
    def handle(self, *args, **options):
        application = get_wsgi_application()
        run(self.addr, self.port, application)
