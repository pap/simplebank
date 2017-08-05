import json

import requests

import time

from nameko.rpc import rpc
from nameko.web.handlers import http
from statsd import StatsClient
from circuitbreaker import circuit
from circuitbreaker import CircuitBreakerMonitor

from pprint import pprint


class DemoService:
    name = "demo_service"

    statsd = StatsClient('localhost', 8125, prefix='simplebank-demo')

    @rpc
    def demo_rpc(self, name):
        return "Hello, {}!".format(name)

    @http('GET', '/get/<int:value>')
    @statsd.timer('demo')
    def demo_http_get(self, request, value):
        return json.dumps({'value': value})

    @http('GET', '/health')
    @statsd.timer('health')
    def health(self, request):
        return json.dumps({'health': 'ok'})

    @http('GET', '/external')
    @circuit(failure_threshold=5, expected_exception=ConnectionError)
    @statsd.timer('external')
    def external_request(self, request):
        r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        return json.dumps({'code': r.status_code, 'body': r.text})

    @http('GET', '/error')
    @circuit(failure_threshold=5, expected_exception=ZeroDivisionError)
    @statsd.timer('error')
    def error_request(self, request):
        return json.dumps({1 / 0})
