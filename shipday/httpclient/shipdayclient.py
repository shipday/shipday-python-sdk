import json

import requests


class ShipdayClient:
    def __init__(self, *args, api_key, **kwargs, ):
        self._api_key = api_key
        self._timeout = kwargs['timeout'] if 'timeout' in kwargs else 1000
        self._base_url = 'https://api.shipday.com/'

    def __get_headers_(self):
        return {
            'Authorization': 'Basic {}'.format(self._api_key),
            'Content-Type': 'application/json',
        }

    def __get_api_key_(self):
        return self._api_key

    def __create_url_(self, suffix: str) -> str:
        return self._base_url + suffix

    def set_api_key(self, api_key: str):
        self._api_key = api_key

    def get(self, suffix: str):
        url = self.__create_url_(suffix)
        response = requests.get(url, headers=self.__get_headers_())
        return response.json()

    def post(self, suffix: str, data: dict):
        url = self.__create_url_(suffix)
        response = requests.post(url, json.dumps(data), headers=self.__get_headers_())
        return response.json()

    def put(self, suffix: str, data: dict):
        url = self.__create_url_(suffix)
        response = requests.put(url, json.dumps(data), headers=self.__get_headers_())
        return response.json()

    def delete(self, suffix: str):
        url = self.__create_url_(suffix)
        response = requests.delete(url, headers=self.__get_headers_())
        return response
