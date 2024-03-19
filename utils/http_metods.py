import json
from requests import Response
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class HttpMethods:
    token = os.getenv('TOKEN_GITHUB')
    payload = {
        "ref": "main",
    }

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    @staticmethod
    def post_token(url) -> Response:
        response = requests.post(
            url=url,
            headers=HttpMethods.headers,
            data=json.dumps(HttpMethods.payload)
        )
        return response
