"""
En liten service for å teste hvordan passerer diverse typer Cookies via Sesam proxy

system setup:

{
  "_id": "test-proxy-headers-forwarding",
  "type": "system:microservice",
  "docker": {
    "image": "<image name>,
    "port": 5000
  },
  "verify_ssl": true
}

for å teste send GET  forespørsel mot https://<node>/api/systems/test-proxy-headers-forwarding/proxy/check_headers_forwarding
og sjekk hvilke av cookies er satt


"""
import json

from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/check_headers_forwarding", methods=["GET"])
def process_request():
    headers = request.headers
    res_headers = {
        "test-header": "presented"
    }
    r = Response(json.dumps(list(headers)), content_type='application/json', headers=res_headers)
    r.set_cookie("test-cookie", "presented")
    r.set_cookie("test-cookie-http-only", "presented", httponly=True)
    r.set_cookie("test-cookie-http-secure", "presented", httponly=True, secure=True)
    return r


if __name__ == '__main__':
    app.run(port=5000, debug=False, host='0.0.0.0')
