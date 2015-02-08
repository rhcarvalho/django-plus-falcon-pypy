import random
from django_demo.wsgi import application as django_app
from falcon_demo.hello import app as falcon_app


falcon_prefix = r'/falcon'
random_prefix = r'/random'

def random_app(environ, start_response):
    return random.choice([falcon_app, django_app])(environ, start_response)

def app(environ, start_response):
    script_name = environ.get('SCRIPT_NAME', '')
    path_info = environ.get('PATH_INFO', '')
    for prefix, app in [(falcon_prefix, falcon_app), (random_prefix, random_app)]:
        if path_info.startswith(prefix):
            prefix_len = len(prefix)
            environ['SCRIPT_NAME'] = script_name + path_info[:prefix_len]
            environ['PATH_INFO'] = path_info[prefix_len:]
            return app(environ, start_response)
    return django_app(environ, start_response)
