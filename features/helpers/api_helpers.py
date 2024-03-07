import logging as log

import requests
from retry import retry
from urllib3.exceptions import ConnectTimeoutError

@retry(ConnectTimeoutError, tries=2, delay=5)
def _make_request(url, context, method):
    try:
        response = requests.request(method, url, headers=context.headers, timeout=30)
        response.raise_for_status()

        if response.text:
            return response.json()
        else:
            return None
    except ConnectTimeoutError as e:
        log.error(f"Connect Timeout Error: {str(e)}")
        raise e