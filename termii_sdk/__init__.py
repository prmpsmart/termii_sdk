from typing import Union
from .messaging_api import (
    Campaigns,
    Contacts,
    Messaging,
    Phonebook,
    SenderID,
    Templates,
    Number,
    Response,
    AddContactResponse,
    FetchCampaignsHistoryResponse,
    FetchCampaignsResponse,
    FetchPhonebooksResponse,
    FetchSenderIDResponse,
    BasicResponse,
)
from .insights_api import (
    EventsAndReport,
    BalanceResponse,
    HistoryResponse,
    SearchResponse,
    StatusResponse,
)
from .token_api import (
    Token,
    EmailTokenResponse,
    InAppTokenResponse,
    SendTokenResponse,
    VerifyTokenResponse,
    VoiceCallResponse,
    VoiceTokenResponse,
)
from .error import Error

__all__ = [
    "TermiiSDK",
    "Error",
    "Response",
    "AddContactResponse",
    "FetchCampaignsHistoryResponse",
    "FetchCampaignsResponse",
    "FetchPhonebooksResponse",
    "FetchSenderIDResponse",
    "BasicResponse",
    "BalanceResponse",
    "HistoryResponse",
    "SearchResponse",
    "StatusResponse",
    "EmailTokenResponse",
    "InAppTokenResponse",
    "SendTokenResponse",
    "VerifyTokenResponse",
    "VoiceCallResponse",
    "VoiceTokenResponse",
]


class TermiiSDK:
    def __init__(self, api_key: str) -> None:
        super().__init__()

        self.events_and_reports = EventsAndReport(api_key)
        self.campaigns = Campaigns(api_key)
        self.contacts = Contacts(api_key)
        self.messaging = Messaging(api_key)
        self.number = Number(api_key)
        self.phonebook = Phonebook(api_key)
        self.senderID = SenderID(api_key)
        self.templates = Templates(api_key)
        self.token = Token(api_key)

    # EventsAndReport
    def balance(self) -> Union[Error, BalanceResponse]:
        return self.events_and_reports.balance()

    def search(self) -> Union[Error, SearchResponse]:
        return self.events_and_reports.search()

    def status(self) -> Union[Error, StatusResponse]:
        return self.events_and_reports.status()

    def history(self) -> Union[Error, HistoryResponse]:
        return self.events_and_reports.history()

    # Campaigns
    def send_campaign(self, **kwargs) -> Union[Error, Response]:
        return self.campaigns.send_campaign(**kwargs)

    def fetch_campaigns(self, **kwargs) -> Union[Error, FetchCampaignsResponse]:
        return self.campaigns.fetch_campaigns(**kwargs)

    def fetch_campaign_history(
        self, **kwargs
    ) -> Union[Error, FetchCampaignsHistoryResponse]:
        return self.campaigns.fetch_campaign_history(**kwargs)

    # Contacts
    def fetch_contacts(self, **kwargs) -> Union[Error, FetchPhonebooksResponse]:
        return self.contacts.fetch_contacts(**kwargs)

    def add_contact(self, **kwargs) -> Union[Error, AddContactResponse]:
        return self.contacts.add_contact(**kwargs)

    def add_contacts(self, **kwargs) -> Union[Error, Response]:
        return self.contacts.add_contacts(**kwargs)

    def delete_contact_phonebook(self, **kwargs) -> Union[Error, Response]:
        return self.contacts.delete_phonebook(**kwargs)

    # Messaging

    def send_message(self, **kwargs) -> Union[Error, BasicResponse]:
        return self.messaging.send_message(**kwargs)

    def send_bulk_message(self, **kwargs) -> Union[Error, BasicResponse]:
        return self.messaging.send_bulk_message(**kwargs)

    # Number
    def send_message_number(self, **kwargs) -> Union[Error, BasicResponse]:
        return self.number.send_message_number(**kwargs)

    # Phonebook
    def fetch_phonebooks(self, **kwargs) -> Union[Error, FetchPhonebooksResponse]:
        return self.phonebook.fetch_phonebooks(**kwargs)

    def create_phonebook(self, **kwargs) -> Union[Error, Response]:
        return self.phonebook.create_phonebook(**kwargs)

    def update_phonebook(self, **kwargs) -> Union[Error, Response]:
        return self.phonebook.update_phonebook(**kwargs)

    def delete_phonebook(self, **kwargs) -> Union[Error, Response]:
        return self.phonebook.delete_phonebook(**kwargs)

    # SenderID
    def fetch_id(self) -> Union[Error, FetchSenderIDResponse]:
        return self.senderID.fetch_id()

    def request_id(self, **kwargs) -> Union[Error, Response]:
        return self.senderID.request(**kwargs)

    # Templates
    def device_template(self, **kwargs) -> Union[Error, BasicResponse]:
        return self.templates.device_template(**kwargs)

    # Token
    def send_token(self, **kwargs) -> Union[Error, SendTokenResponse]:
        return self.token.send_token(**kwargs)

    def voice_token(self, **kwargs) -> Union[Error, VoiceTokenResponse]:
        return self.token.voice_token(**kwargs)

    def voice_call(self, **kwargs) -> Union[Error, VoiceCallResponse]:
        return self.token.voice_call(**kwargs)

    def in_app_token(self, **kwargs) -> Union[Error, InAppTokenResponse]:
        return self.token.in_app_token(**kwargs)

    def verify_token(self, **kwargs) -> Union[Error, VerifyTokenResponse]:
        return self.token.verify_token(**kwargs)

    def email_token(self, **kwargs) -> Union[Error, EmailTokenResponse]:
        return self.token.email_token(**kwargs)
