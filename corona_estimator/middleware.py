from buildForSDG.settings import BASE_DIR
from datetime import datetime, timedelta
import time, os



class LogMiddleware(object):
    def process_request(self, request):
        request.start_time = datetime.now()

    def process_response(self, request, response):
        total = datetime.now() - request.start_time
        with open(os.path.join(BASE_DIR, 'log'), 'a', newline='') as file:
            message = f'{request.method} {request.path} {int(total * 1000)}\n'
            file.write(message)
        file.close()

        return response
        
    