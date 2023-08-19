"""Constants used in the library
__author_github__ = https://github.com/prmpsmart
__author__ = prmpsmart@gmail.com
"""


from .core import Json, Request, RequestType, Response


# -----------------------------------
# Responses classes


class BalanceResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.user: str = json.user
        self.balance: int = json.balance
        self.currency: str = json.currency


class SearchResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.number: str = json.number
        self.status: str = json.status
        self.network: str = json.network
        self.network_code: str = json.network_code


class RouteDetail:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.number: str = json.number
        self.ported: str = json.ported


class CountryDetail:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.countryCode: str = json.countryCode
        self.mobileCountryCode: str = json.mobileCountryCode
        self.iso: str = json.iso


class OperatorDetail:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.operatorCode: str = json.operatorCode
        self.operatorName: str = json.operatorName
        self.mobileNumberCode: str = json.mobileNumberCode
        self.mobileRoutingCode: str = json.mobileRoutingCode
        self.carrierIdentificationCode: str = json.carrierIdentificationCode
        self.lineType: str = json.lineType


class StatusResult:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.routeDetail: RouteDetail = RouteDetail(json.routeDetail)
        self.countryDetail: CountryDetail = CountryDetail(json.countryDetail)
        self.operatorDetail: OperatorDetail = OperatorDetail(json.operatorDetail)
        self.status: int = json.status


class StatusResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.result: list[StatusResult] = []
        for result in json.result:
            self.result.append(StatusResult(result))


class HistoryResult:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.sender: str = json.sender
        self.receiver: str = json.receiver
        self.message: str = json.message
        self.amount: int = json.amount
        self.reroute: int = json.reroute
        self.status: str = json.status
        self.sms_type: str = json.sms_type
        self.send_by: str = json.send_by
        self.media_url: str = json.media_url
        self.message_id: str = json.message_id
        self.notify_url: str = json.notify_url
        self.notify_id: str = json.notify_id
        self.created_at: str = json.created_at


class HistoryResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.results: list[HistoryResult] = []

        for result in json:
            self.result.append(HistoryResult(result))


# -----------------------------------
# Request classes


class EventsAndReport(Request):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def balance(self) -> BalanceResponse:
        "The Balance API returns your total balance and balance information from your wallet, such as currency."

        return self.make_request(
            requests_type=RequestType.GET,
            path="get-balance",
            response_class=BalanceResponse,
        )

    def search(self, phone_number: str):
        "The search API allows businesses verify phone numbers and automatically detect their status as well as current network. It also tells if the number has activated the do-not-disturb settings."

        return self.make_request(
            requests_type=RequestType.GET,
            path="check/dnd",
            params=Json(phone_number=phone_number),
            response_class=SearchResponse,
        )

    def status(
        self,
        phone_number: str,
        country_code: str,
    ):
        "The status API allows businesses to detect if a number is fake or has ported to a new network."

        return self.make_request(
            requests_type=RequestType.GET,
            path="insight/number/query",
            params=Json(
                phone_number=phone_number,
                country_code=country_code,
            ),
            response_class=SearchResponse,
        )

    def history(self):
        "This Inbox API returns reports for messages sent across the sms, voice & whatsapp channels. Reports can either display all messages on termii or a single message."

        return self.make_request(
            requests_type=RequestType.GET,
            path="sms/inbox",
            response_class=SearchResponse,
        )
