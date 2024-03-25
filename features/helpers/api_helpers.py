import logging as log

import requests
from retry import retry
from urllib3.exceptions import ConnectTimeoutError

@retry(ConnectTimeoutError, tries=2, delay=5)
def _make_request(url, context, method , data):
    try:
        log.info(f"Making a {method} request to {url}")
        response = requests.request(method, url, timeout=30, data= data if method == "POST" else None)
        
        return response

    except ConnectTimeoutError as e:
        log.error(f"Connect Timeout Error: {str(e)}")
        raise e