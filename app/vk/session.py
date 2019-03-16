# -*- coding: utf-8 -*-

from app import logging
import requests
import logging


class Session:
    def __init__(self, token, version=5.98):
        self.session = requests.Session()
        self.session.params.update({"access_token": token})
        self.session.params.update({"v": version})
        logging.debug(f"Параметры запроса сессии: {self.session.params}.")

    def get(self, endpoint, params=None, headers=None):
        endpoint = endpoint if endpoint.startswith("https") else f"https://api.vk.com/method/{endpoint}"
        logging.debug(f"Эндпоинт, куда будет сделан запрос: {endpoint}")

        response = self.session.get(endpoint, params=params, headers=headers)
        return response.json()

    def post(self, endpoint, params=None, headers=None):
        endpoint = endpoint if endpoint.startswith("https") else f"https://api.vk.com/method/{endpoint}"
        logging.debug(f"Эндпоинт, куда будет сделан запрос: {endpoint}")

        response = self.session.post(endpoint, params=params, headers=headers)
        return response.json()
