from django.core.management.base import NoArgsCommand
from historylink.manager import manager




class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        manager.syncAll()
        