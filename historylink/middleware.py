from django.http import Http404, HttpResponsePermanentRedirect


from historylink.models import HistoryLink as HistoryLinkModel

class HistoryLink(object):
    
    def process_exception(self, request, exception):
        
        if isinstance(exception, Http404):
            try:
                hl = HistoryLinkModel.objects.get(url=request.META.get('PATH_INFO'))
                
                if request.META.get('PATH_INFO') != hl.content_object.get_absolute_url():                
                    return HttpResponsePermanentRedirect(redirect_to=hl.content_object.get_absolute_url())
            except:
                return
            
            