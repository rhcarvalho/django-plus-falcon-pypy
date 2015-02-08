import json
import sys
import platform
import datetime
from pprint import pformat

import falcon


class HelloResource(object):
    def on_get(self, req, resp):
        resp.body = "\n".join([
            "Hello from Falcon!",
            datetime.datetime.utcnow().isoformat(),
            "",
            platform.platform(),
            "Python " + sys.version
        ])


class JSONResource(object):
    encode = json.JSONEncoder(
        check_circular=False,
        separators=(',', ':'),
    ).encode

    def on_get(self, req, resp):
        resp.body = self.encode({"hello": "world"})


def not_found(req, resp):
    resp.body = "%s(%s)" % (
        req.__class__.__name__,
        pformat({atrr: getattr(req, atrr) for atrr in req.__slots__})
    )


app = falcon.API()
app.add_route('/', HelloResource())
app.add_route('/json', JSONResource())
app.add_sink(not_found)
