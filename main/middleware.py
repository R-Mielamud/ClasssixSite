from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from time import time

class AntispamMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if (request.path != "/stop_spam/" 
                and request.path != "/favicon.ico"
                and request.path != "/static/"): 
                    if not request.session.get("request_count"):
                        request.session["request_count"] = 1
                    else:
                        request.session["request_count"] += 1

        if request.session.get("request_time"):
            if ((request.session.get("request_time") - time()) <= 4
                and request.session.get("request_count") > 17
                and request.path != "/stop_spam/" 
                and request.path != "/favicon.ico"
                and request.path != "/static/"):
                    request.session["request_count"] = 1
                    request.session["request_time"] = time()
                    return redirect("/stop_spam/")
            elif (request.session.get("request_time") - time()) > 4:
                request.session["request_count"] = 1
                request.session["request_time"] = time()
        else:
            request.session["request_time"] = time()

    def process_response(self, request, response):
        return response

class ErrorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_response(self, request, response):
        if response.status_code >= 400:
            return redirect("/error/{}/{}/".format(response.status_code, response.reason_phrase))

        return response
