from urllib.parse import urljoin

import requests
from requests import HTTPError, Response
from api.retry import retry

from api.token_provider import TokenProvider


class ApiClient:
    """ Base class for api clients """
    def __init__(self, base_url: str, token_provider: TokenProvider = None):
        """ Initialize an api client by its base url """
        self.base_url = base_url
        self.token_provider = token_provider or TokenProvider()
    
    @retry(max_attempts=3, initial_delay_ms=1000, transient_error=HTTPError, http_error_code=[429, 500, 502, 503, 524])
    def get(self, endpoint: str, params: dict = None, **kwargs) -> Response:
        """Make http get request

        Args:
            endpoint (str): the endpoint to the base url. ex: "assets/data/query"
            params (dict, optional): query parameters to be appended to the end of the url. Defaults to None.
                Note that in get requests, there is a limit on query params length. Be careful when you're passing 
                a long parameter list. 

        Returns:
            Response: response of the http request. Response code with 400 and 500 will be raised automatically.
        """
        print(f"hitting endpoint {endpoint}")
        url = self.build_url(endpoint)
        headers = self.build_headers()
        res = requests.get(url, headers=headers, params=params, **kwargs)
        res.raise_for_status()
        return res

    @retry(max_attempts=3, initial_delay_ms=1000, transient_error=HTTPError, http_error_code=[429, 500, 502, 503, 524])
    def post(self, endpoint: str, params: dict = None, data: dict = None, json: dict = None, **kwargs) -> Response:
        """Make http post request. 
        Note that json and data are almost the same, except that when using json 
        the content-type in request headers will be automatically set as application/json.

        Args:
            endpoint (str): the endpoint to the base url. ex: "assets/data/query"
            params (dict, optional): query parameters to be appended to the end of the url. Defaults to None.
                Note that in get requests, there is a limit on query params length. Be careful when you're passing 
                a long parameter list.
            data (dict, optional): Request body. Defaults to None.
            json (dict, optional): Request body. Defaults to None.
                Note that json and data are almost the same, except that when using json, the content-type request header 
                will be automatically set to application/json.

        Returns:
            Response: response of the http request. Response code with 400 and 500 will be raised automatically.
        """
        url = self.build_url(endpoint)
        headers = self.build_headers()
        res = requests.post(url, headers=headers, params=params, data=data, json=json, **kwargs)
        res.raise_for_status()
        return res

    def build_url(self, endpoint: str) -> str:
        """ Build complete url for the endpoint """
        return urljoin(self.base_url, endpoint)

    def build_headers(self):
        """ build headers by injecting the token """
        method = self.token_provider.auth_method
        token = self.token_provider.get_token()
        return {
            "Authorization": f"{method} {token}",
            "Content-Type": "application/json"    
        }
