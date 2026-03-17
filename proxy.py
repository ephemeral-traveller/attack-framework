import logging

from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    logging.log(logging.INFO, f"Request: {flow.request.host}")


def response(flow: http.HTTPFlow) -> None:
    # remove security head
    for header in ['Strict-Transport-Security', 'Content-Security-Policy']:
        if header in flow.response.headers:
            del flow.response.headers[header]
