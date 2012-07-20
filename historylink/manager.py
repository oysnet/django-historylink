from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType

from historylink.models import HistoryLink

class AlreadyRegistered(Exception):
    pass


class ModelManager(object):
    
    def post_save(self, sender, instance, created, **kwargs):
        self.createHistoryLink(instance)
        
    def post_delete(self, sender, instance, **kwargs):
        HistoryLink.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.pk).delete()

    
    def createHistoryLink(self, o):
        HistoryLink.objects.get_or_create(content_type=ContentType.objects.get_for_model(o), 
                                                  object_id=o.pk, url=o.get_absolute_url(), 
                                                  defaults={'content_object' : o, 
                                                            'url' : o.get_absolute_url()})
    

class Manager(object):
    
    _registry = {}
    
    def register(self, models, manager=ModelManager):
        
        if not isinstance(models, (list, tuple,)):
            models = [models]
        
        for model in models:
            
            if model in self._registry:
                continue
            
            self._registry[model] = manager()
            
            post_save.connect(self._registry[model].post_save, sender=model)
            post_delete.connect(self._registry[model].post_delete, sender=model)
            
    def syncModel(self, model):
        
        ct = ContentType.objects.get_for_model(model)
        manager = self._registry.get(model)
        query = model.objects.all()
            
        print "syncing %s.%s (%s objects)" % (ct.app_label, ct.name, query.count())
        
        for o in query:
            manager.createHistoryLink(o)
        
    def syncAll(self):
        
        for model, manager in self._registry.iteritems():
            
            ct = ContentType.objects.get_for_model(model)
            
            query = model.objects.all()
            
            print "syncing %s.%s (%s objects)" % (ct.app_label, ct.name, query.count())
            
            for o in query:
                manager.createHistoryLink(o)
    
manager = Manager()