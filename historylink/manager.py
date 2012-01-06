from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType

from historylink.models import HistoryLink

class AlreadyRegistered(Exception):
    pass

class Manager(object):
    
    _registry = []
    
    def register(self, *args):
        for model in args:
            
            if model in self._registry:
                continue
            
            self._registry.append(model)
            
            post_save.connect(self.post_save, sender=model)
            post_delete.connect(self.post_delete, sender=model)
            
    def post_save(self, sender, instance, created, **kwargs):
        self._createHistoryLink(instance)
        
    def post_delete(self, sender, instance, **kwargs):
        HistoryLink.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.pk).delete()

    
    def _createHistoryLink(self, o):
        HistoryLink.objects.get_or_create(content_type=ContentType.objects.get_for_model(o), 
                                                  object_id=o.pk, url=o.get_absolute_url(), 
                                                  defaults={'content_object' : o, 
                                                            'url' : o.get_absolute_url()})
        
    def syncAll(self):
        
        for model in self._registry:
            
            ct = ContentType.objects.get_for_model(model)
            
            query = model.objects.all()
            
            print "syncing %s.%s (%s objects)" % (ct.app_label, ct.name, query.count())
            
            for o in query:
                self._createHistoryLink(o)
    
manager = Manager()