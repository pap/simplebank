import json
from nameko.web.handlers import http
from nameko.rpc import rpc


class DemoService:
    name = "demo_service"

    @rpc
    def hello_rpc(self, name):
        return "Hello, {}!".format(name)

    @http('GET', '/get/<int:value>')
    def hello_http(self, request, value):
        return json.dumps({'value': value})
