"""
Constants used in the library
__author_github__ = https://github.com/prmpsmart
__author__ = prmpsmart@gmail.com
"""

from .core import (
    Json,
    BasicResponse,
    Response,
    Enum,
    Channel,
    Request,
    RequestType,
    MessageType,
)


# -----------------------------------
# Enum classes


class MediaType(Enum):
    IMAGE = "generic"
    AUDIO = "dnd"
    DOCUMENTS = "whatsapp"
    VIDEO = "whatsapp"
    PLAIN = "plain"


# -----------------------------------
# Data classes


class CampaignsData:
    def __init__(self, json: Json) -> None:
        self.campaign_id: str = json.campaign_id
        self.phone_book: str = json.phone_book
        self.sender: str = json.sender
        self.camp_type: str = json.camp_type
        self.channel: str = json.channel
        self.total_recipients: int = json.total_recipients
        self.run_at: str = json.run_at
        self.status: str = json.status
        self.created_at: str = json.created_at


class CampaignsHistoryData:
    def __init__(self, json: Json) -> None:
        self.id: int = json.id
        self.sender: str = json.sender
        self.receiver: str = json.receiver
        self.message: str = json.message
        self.message_abbreviation: str = json.message_abbreviation
        self.amount: int = json.amount
        self.channel: str = json.channel
        self.sms_type: str = json.sms_type
        self.message_id: str = json.message_id
        self.status: str = json.status
        self.date_created: str = json.date_created
        self.last_updated: str = json.last_updated


class ContactsData:
    def __init__(self, json: Json) -> None:
        self.id: int = json.id
        self.pid: int = json.pid
        self.phone_number: str = json.phone_number
        self.email_address: str = json.email_address
        self.message: str = json.message
        self.company: str = json.company
        self.first_name: str = json.first_name
        self.last_name: str = json.last_name
        self.create_at: str = json.create_at
        self.updated_at: str = json.updated_at


class PhonebooksMeta:
    def __init__(self, json: Json) -> None:
        self.current_page: int = json.current_page
        self.from_: int = json.from_
        self.last_page: int = json.last_page
        self.path: str = json.path
        self.per_page: int = json.per_page
        self.to: int = json.to
        self.total: int = json.total


class PhonebooksLinks:
    def __init__(self, json: Json) -> None:
        self.first: str = json.first
        self.last: str = json.last
        self.prev: str = json.prev
        self.next: str = json.next


class PhonebooksData:
    def __init__(self, json: Json) -> None:
        self.id: str = json.id
        self.name: str = json.name
        self.total_number_of_contacts: int = json.total_number_of_contacts
        self.date_created: str = json.date_created
        self.last_updated: str = json.last_updated


class SenderIDData:
    def __init__(self, json: Json) -> None:
        super().__init__()

        self.sender_id: str = json.sender_id
        self.status: str = json.status
        self.company: str = json.company
        self.usecase: str = json.usecase
        self.country: str = json.country
        self.created_at: str = json.created_at


# -----------------------------------
# Responses classes


class AddContactResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.data: ContactsData = ContactsData(json.data)


class FetchCampaignsHistoryResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.links: PhonebooksLinks = PhonebooksLinks(json.links)
        self.meta: PhonebooksMeta = PhonebooksMeta(json.meta)

        self.data: CampaignsHistoryData = CampaignsHistoryData(json.data)


class FetchCampaignsResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.links: PhonebooksLinks = PhonebooksLinks(json.links)
        self.meta: PhonebooksMeta = PhonebooksMeta(json.meta)

        self.data: list[CampaignsData] = []

        for data in json.data:
            self.data.append(CampaignsData(data))


class FetchContactsResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.links: PhonebooksLinks = PhonebooksLinks(json.links)
        self.meta: PhonebooksMeta = PhonebooksMeta(json.meta)

        self.data: list[ContactsData] = []

        for data in json.data:
            self.data.append(ContactsData(data))


class FetchCampaignsResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.links: PhonebooksLinks = PhonebooksLinks(json.links)
        self.meta: PhonebooksMeta = PhonebooksMeta(json.meta)

        self.data: list[CampaignsData] = []

        for data in json.data:
            self.data.append(CampaignsData(data))


class FetchPhonebooksResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.links: PhonebooksLinks = PhonebooksLinks(json.links)
        self.meta: PhonebooksMeta = PhonebooksMeta(json.meta)

        self.data: list[PhonebooksData] = []

        for data in json.data:
            self.data.append(PhonebooksData(data))


class FetchSenderIDResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.current_page: int = json.current_page
        self.first_page_url: str = json.first_page_url
        self.from_: int = json.from_
        self.last_page: int = json.last_page
        self.last_page_url: str = json.last_page_url
        self.next_page_url: str = json.next_page_url
        self.path: str = json.path
        self.per_page: int = json.per_page
        self.prev_page_url: str = json.prev_page_url
        self.to: int = json.to
        self.total: int = json.total

        self.data: list[SenderIDData] = []

        for data in json.data:
            self.data.append(SenderIDData(data))


# -----------------------------------
# Request classes


class Campaigns(Request):
    """Using our campaign APIs, you can view, manage and send a campaign to a phonebook."""

    endpoint = "sms/campaigns"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def send_campaign(
        self,
        *,
        country_code: str,
        sender_id: str,
        message: str,
        channel: Channel,
        message_type: MessageType,
        phonebook_id: str,
        delimiter: str,
        remove_duplicate: str,
        campaign_type: str,
        schedule_time: str = "",
        schedule_sms_status: str = "",
    ) -> Response:
        if schedule_sms_status:
            assert schedule_sms_status == "scheduled"
        else:
            schedule_time = ""

        return self.make_request(
            requests_type=RequestType.POST,
            path="send",
            json=Json(
                country_code=country_code,
                sender_id=sender_id,
                message=message,
                channel=channel.value,
                message_type=message_type.value,
                phonebook_id=phonebook_id,
                delimiter=delimiter,
                remove_duplicate=remove_duplicate,
                campaign_type=campaign_type,
                schedule_time=schedule_time,
                schedule_sms_status=schedule_sms_status,
            ),
        )

    def fetch_campaigns(self) -> FetchCampaignsResponse:
        return self.make_request(
            requests_type=RequestType.GET,
            response_class=FetchCampaignsResponse,
        )

    def fetch_campaign_history(self, campaign_id: str) -> FetchCampaignsHistoryResponse:
        return self.make_request(
            requests_type=RequestType.GET,
            path=campaign_id,
            response_class=FetchCampaignsHistoryResponse,
        )


class Contacts(Request):
    """Contacts API allows you manage (i.e. edit, update, & delete) contacts in your phonebook."""

    endpoint = "phonebooks"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def fetch_contacts(self, phonebook_id: str) -> FetchPhonebooksResponse:
        return self.make_request(
            requests_type=RequestType.GET,
            path=f"{phonebook_id}/contacts",
            response_class=FetchPhonebooksResponse,
        )

    def add_contact(
        self,
        *,
        phonebook_id: str,
        phone_number: str,
        email_address: str,
        first_name: str,
        last_name: str,
        company: str,
        country_code: str,
    ) -> AddContactResponse:
        return self.make_request(
            requests_type=RequestType.POST,
            path=f"{phonebook_id}/contacts",
            json=Json(
                phone_number=phone_number,
                email_address=email_address,
                first_name=first_name,
                last_name=last_name,
                company=company,
                country_code=country_code,
            ),
            response_class=AddContactResponse,
        )

    def add_contacts(
        self,
        *,
        phonebook_id: str,
        contact_file: str,
        country_code: str,
    ) -> Response:
        return self.make_request(
            requests_type=RequestType.PATCH,
            path=f"{phonebook_id}/contacts",
            json=Json(
                contact_file=contact_file,
                country_code=country_code,
            ),
        )

    def delete_phonebook(self, *, contact_id: str) -> Response:
        return self.make_request(
            requests_type=RequestType.DELETE,
            path=f"contacts/{contact_id}",
        )


class Messaging(Request):
    """This API allows businesses send text messages to their customers across different messaging channels. The API accepts JSON request payload and returns JSON encoded responses, and uses standard HTTP response codes."""

    endpoint = "sms/send"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def send_message(
        self,
        *,
        to: str,
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
        type: MediaType = MediaType.PLAIN,
        media_url: str = "",
        media_caption: str = "",
    ) -> BasicResponse:
        assert [bool(sms), bool(media_url)].count(
            True
        ) == 1, "Only one of sms or media_url is allowed."

        media = Json()
        if media_url:
            media = Json(
                url=media_url,
                caption=media_caption,
            )
        json = Json(
            to=to,
            sms=sms,
            type=type.value,
            channel=channel.value,
            media=media,
        )
        json["from"] = from_

        return self.make_request(
            requests_type=RequestType.POST,
            json=json,
            response_class=BasicResponse,
        )

    def send_bulk_message(
        self,
        *,
        to: list[str],
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
    ) -> BasicResponse:
        json = Json(
            to=to,
            sms=sms,
            type=MediaType.PLAIN,
            channel=channel.value,
        )
        json["from"] = from_

        return self.make_request(
            requests_type=RequestType.POST,
            path="bulk",
            json=json,
            response_class=BasicResponse,
        )


class Number(Request):
    """This API allows businesses send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location."""

    endpoint = "sms/number/send"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def send_message_number(
        self,
        *,
        to: str,
        sms: str = "",
    ) -> BasicResponse:
        json = Json(
            to=to,
            sms=sms,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            json=json,
            response_class=BasicResponse,
        )


class Phonebook(Request):
    """Create, view & manage phonebooks using these APIs. Each phonebook can be identified by a unique ID, which makes it easier to edit or delete a phonebook."""

    endpoint = "phonebooks"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def fetch_phonebooks(self)->FetchPhonebooksResponse:
        return self.make_request(
            requests_type=RequestType.GET,
            response_class=FetchPhonebooksResponse,
        )

    def create_phonebook(
        self,
        *,
        phonebook_name: str,
        description: str,
    )->Response:
        return self.make_request(
            requests_type=RequestType.POST,
            json=Json(
                phonebook_name=phonebook_name,
                description=description,
            ),
        )

    def update_phonebook(
        self,
        *,
        phonebook_id: str,
        phonebook_name: str,
        description: str,
    )->Response:
        return self.make_request(
            requests_type=RequestType.PATCH,
            path=phonebook_id,
            json=Json(
                phonebook_name=phonebook_name,
                description=description,
            ),
        )

    def delete_phonebook(
        self,
        *,
        phonebook_id: str,
    )->Response:
        return self.make_request(
            requests_type=RequestType.DELETE,
            path=phonebook_id,
        )


class SenderID(Request):
    """A Sender ID is the name or number that identifies the sender of an SMS message. This API allows businesses retrieve the status of all registered sender ID and request registration of sender ID through GET and POST request type respectively."""

    endpoint = "sender-id"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def fetch_id(self)->FetchSenderIDResponse:
        return self.make_request(
            requests_type=RequestType.GET,
            response_class=FetchSenderIDResponse,
        )

    def request(
        self,
        *,
        sender_id: str,
        usecase: str,
        company: str,
    )->Response:
        return self.make_request(
            requests_type=RequestType.POST,
            path="request",
            json=Json(
                sender_id=sender_id,
                usecase=usecase,
                company=company,
            ),
        )


class Templates(Request):
    """Templates API helps businesses set a template for the one-time-passwords (pins) sent to their customers via whatsapp or sms."""

    endpoint = "send/template"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def device_template(
        self,
        *,
        phone_number: str,
        device_id: str,
        template_id: str,
        data: Json = None,
    ):
        json = Json(
            phone_number=phone_number,
            device_id=device_id,
            template_id=template_id,
            data=data or Json(),
        )

        return self.make_request(
            requests_type=RequestType.POST,
            json=json,
            response_class=BasicResponse,
        )
