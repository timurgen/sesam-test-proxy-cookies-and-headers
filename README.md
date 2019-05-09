# sesam-test-proxy-cookies-and-headers
En liten service for å teste hvordan passerer diverse typer Cookies via Sesam proxy

system setup:
```
{
  "_id": "test-proxy-headers-forwarding",
  "type": "system:microservice",
  "docker": {
    "image": "<image name>,
    "port": 5000
  },
  "verify_ssl": true
}
```
for å teste send GET  forespørsel mot https://<node>/api/systems/test-proxy-headers-forwarding/proxy/check_headers_forwarding
og sjekk hvilke av cookies er satt
