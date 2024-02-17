"""Constants used in the library
__author_github__ = https://github.com/prmpsmart
__author__ = prmpsmart@gmail.com
"""


import requests
from http import HTTPStatus
from typing import Union, Any
from enum import Enum


# -----------------------------------
# Constants


TERMII_ENDPOINT = "https://api.ng.termii.com/api"


# -----------------------------------
# Enum classes


class Channel(Enum):
    GENERIC = "generic"
    DND = "dnd"
    WHATSAPP = "whatsapp"


class MessageType(Enum):
    NUMERIC = "NUMERIC"
    ALPHANUMERIC = "ALPHANUMERIC"


class RequestType(Enum):
    """RequestType for the requests"""

    DELETE = "DELETE"
    GET = "GET"
    PATCH = "PATCH"
    POST = "POST"


# -----------------------------------
# Data classes


class Json(dict):
    def __getattr__(self, __key: Any) -> Any:
        if __key == "from_":
            __key = "from"
        return super().__getitem__(__key)


# -----------------------------------
# Responses classes


class Response:
    def __init__(self, json: Json) -> None:
        self.code = json.code
        self.message = json.message


class BasicResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.message_id: str = json.message_id
        self.balance: int = json.balance
        self.user: str = json.user


# -----------------------------------
# Error classes


class Error:
    def __init__(self, response: requests.Response) -> None:
        self.raw_response = response


# -----------------------------------
# Request class


class Request:
    termii_endpoint = TERMII_ENDPOINT
    timeout: int = 5
    endpoint: str = ""

    def __init__(self, api_key: str) -> None:
        super().__init__()

        self.api = Json(api_key=api_key)

    def make_request(
        self,
        *,
        requests_type: RequestType,
        path: str = "",
        endpoint: str = "",
        params: Json = None,
        json: Json = None,
        timeout: int = 0,
        response_class: Response = Response,
    ) -> Union[Error, Response]:
        "returns the str of the requests_type"

        termii_endpoint = self.termii_endpoint.strip().rstrip()
        endpoint = endpoint or self.endpoint
        endpoint = self.endpoint.strip().rstrip()
        path = path.strip().rstrip()

        url = f"{termii_endpoint}/{endpoint}"
        if path:
            url += f"/{path}"

        if requests_type == RequestType.POST:
            json.update(self.api)
        else:
            params = params.update(self.api) if params else self.api

        response = requests.request(
            requests_type.value,
            url,
            timeout=timeout or self.timeout,
            params=params,
            json=json,
            headers={
                "Content-Type": "application/json",
            },
        )

        if response_class and response.status_code == HTTPStatus.OK:
            return response_class(response.json(object_hook=Json))
        else:
            return Error(response)
