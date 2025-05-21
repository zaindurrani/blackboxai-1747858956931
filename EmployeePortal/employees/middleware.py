import logging

logger = logging.getLogger(__name__)

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed before the view
        logger.info("SimpleMiddleware: Processing request before view")
        
        response = self.get_response(request)
        
        # Code to be executed after the view
        logger.info("SimpleMiddleware: Processing request after view")
        
        return response
