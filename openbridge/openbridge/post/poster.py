"""
Main purpose it to send a POST request to a given URL

send_json_post_request(payload, url)
    1. check if payload satisfies serialization format
    2. check if url is in right format
    3. send a payload to the url
    4. get and return response from the server
"""

import json

import requests
import jsonschema
try:
    import rfc3987
except ImportError:
    pass
import logging
import time, sys

logging.basicConfig()
log = logging.getLogger()

SCHEME = 'https'
DOMAIN = 'api.openbridge.io'
PATH = 'user'
SCHEMA = {
    "properties": {
        "api_key": {
            "type": "string"
        }
    },
    "required": [
        "api_key"
    ],
    "title": "payload schema",
    "type": "object"
}


def send_json_post_request(payload, url, force_url_checking=True):
    """
    Send payload in a given serialization format

    :type payload: dict
    :param payload: A dictionary of key value pairs that will be send to the system.

    :type url: string
    :param url: A url that was provided by openbridge.

    :type force_url_checking: bool
    :param force_url_checking: If set to true than url will be forced to follow SCHEME,
    DOMAIN and PATH, specified above. If False, then post request will be sent to the "url"

    :rtype: int
    :return: HTTP response codea.
    """
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    pld = convert_payload(payload, serialization='JSON')
    if force_url_checking:
        check_url(url)
    response = make_request(headers, url, pld)
    return response

def make_request(headers, url, payload, max_retries=5):
    """
    Return response from url.
    Retry up to 5 times for server errors. Sleep 30 seconds between retries
    Do not retrie client-side errors.

    :type headers: dict
    :param headers: A dictionary of standart HTTP request headers

    :type url: string
    :param url: A url, that was provided by openbridge.

    :type payload: dict
    :param payload: A dictionary of key value pairs will be send to the system.

    :type max_retries: int
    :param max_retries: Number of times retry to connect.

    :rtype: requests.Response
    :return: Response from request
    """
    response = None
    response = requests.post(url, data=payload, verify=False,
                             headers=headers)
    if response.status_code > 499:
        time.sleep(1)
        if retries == max_retries:
            log.error("downloading %s: server-side error (%d)" %
                      (url, response.status_code))
            return response
    elif response.status_code > 399:
        log.error("downloading %s: client-side error (%d)" %
                  (url, response.status_code))
        return response
    return response


def convert_payload(payload, serialization):
    """
    Serializes payload

    :type payload: dict
    :param payload: A dictionary of key value pairs that will be checked.

    :type serialization: string
    :param serialization: Kind of a data filter.
        Valid values are currently:

            * JSON

    :rtype: string
    :return: String representation of JSON
    """
    if serialization == 'JSON':
        if isinstance(payload, dict):
            try:
                jsonschema.validate(payload, SCHEMA)
                pld = json.dumps(payload)
                return pld
            except (TypeError, ValueError) as err:
                 logging.error('ERROR % ' % err)
        else:
            raise Exception('Payload is not a valid python dictionary')

def check_url(url):
    """
    Check if url satisfies URI format and contains valid scheme and domain

    :type url: string
    :param url: Provided URL
    """
    scheme = SCHEME
    domain = DOMAIN
    path = PATH

    if not 'rfc3987' in sys.modules:
        if (scheme+'://' and domain) in url:
            return True
        else:
            raise Exception("URL %s should begin with %s://%s" % (url,
                                                                  scheme,
                                                                  domain))

    pieces = rfc3987.parse(url, 'URI')
    if scheme != pieces['scheme']:
        raise Exception('%s should be %s' % (pieces['scheme'], SCHEME))
    if domain != pieces['authority']:
        raise Exception('%s should be %s' %(pieces['authority'], DOMAIN))
    if path != pieces['path'].split('/')[1]:
        raise Exception('URL should start with %s://%s%s' % (SCHEME,
                                                             DOMAIN,
                                                             PATH))
    return True


















