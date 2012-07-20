from django.core.management.base import  BaseCommand
from historylink.manager import manager
from django.contrib.contenttypes.models import ContentType




class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        if len(args) > 0:
            
            for arg in args:
                model = ContentType.objects.get_by_natural_key(*arg.split('.')).model_class()
                manager.syncModel(model)
                
        else:
            manager.syncAll()
        