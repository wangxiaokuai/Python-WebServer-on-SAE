import sae
import json
from counter import Counter

from cgi import parse_qs

## A wsgi applacation.
## for test in a browser: http://wangxiaokuai.applinzi.com/?key=wangxiaokuai
def simple_app(environ, start_response):
    """Simplest possible application object"""

    # parse query string

    query_dict = parse_qs(environ["QUERY_STRING"])  

    key = query_dict.get("key", [""]).pop(0)

    counter = Counter(key)
    counter.increase()
    data = {}
    data["key"] = key
    data["total_points"] = counter.get()

    status = '200 OK'
    response_headers = [('Content-type','application/json')]
    response_headers.append(("Access-Control-Allow-Origin", "*"))
    
    start_response(status, response_headers)
    return json.dumps(data)

application = sae.create_wsgi_app(simple_app)