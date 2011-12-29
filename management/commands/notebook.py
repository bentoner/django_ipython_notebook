import os
from django.core.management.base import BaseCommand
from optparse import make_option

DEFAULT_PORT = "8888"

class Command(BaseCommand):
    args = '[optional port number, or ipaddr:port]'
    option_list = BaseCommand.option_list
    help = "Runs the IPython notebook."
    requires_model_validation = False

    def handle(self, addrport='', *args, **options):
        if args:
            raise CommandError('Usage is notebook %s' % self.args)
        
        if not addrport:
            self.addr = ''
            self.port = DEFAULT_PORT
        # TODO Pass port and address to IPython.

        # Can't work out how to embed ipython in this python process so just
        # launch another process.
        code_to_run = """import settings
import django.core.management
django.core.management.setup_environ(settings)
"""
        os.system('ipython notebook -c "%s"' % code_to_run)
