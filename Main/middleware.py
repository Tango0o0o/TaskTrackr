from django.http import HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.contrib import messages

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, req):
        # Code to be executed for each req before
        # the view (and later middleware) are called.

        response = self.get_response(req)

        # Code to be executed for each req/response after
        # the view is called.

        # if response.status_code == 500:
        #     response = render(req, "Main/status_500.html")
        # elif response.status_code == 404:
        #     response = render(req, "Main/status_404.html")
            
        return response