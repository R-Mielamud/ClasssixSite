from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from time import time

class ErrorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if response.status_code >= 400:
            return redirect("/error/{}/{}/".format(response.status_code, response.reason_phrase))

        return response
