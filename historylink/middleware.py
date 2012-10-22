from django.http import Http404, HttpResponsePermanentRedirect


from historylink.models import HistoryLink as HistoryLinkModel

class HistoryLink(object):
    """
    def process_exception(self, request, exception):
        
        if isinstance(exception, Http404):
            import pdb; pdb.set_trace()
            try:
                hl = HistoryLinkModel.objects.get(url=request.META.get('PATH_INFO'))
                
                if request.META.get('PATH_INFO') != hl.content_object.get_absolute_url():                
                    return HttpResponsePermanentRedirect(redirect_to=hl.content_object.get_absolute_url())
            except:
                return
            
    """        
            
    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for a redirect for non-404 responses.
        path_qs = request.get_full_path().split('?')
        
        path = path_qs[0]
        if len(path_qs) > 1:
            qs = "?" + '?'.join(path_qs[1:])
        else:
            qs = ''
            
        try:
            hl = HistoryLinkModel.objects.get(url=path)
            
            if path != hl.content_object.get_absolute_url():                
                return HttpResponsePermanentRedirect(redirect_to="%s%s" %( hl.content_object.get_absolute_url(), qs))
        except:
            pass

        # No redirect was found. Return the response.
        return response
