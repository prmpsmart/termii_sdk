# Termii SDK Documentation

Welcome to the Termii SDK documentation! This SDK provides a Python interface for integrating with the Termii API, allowing you to send SMS, voice, and email messages easily within your applications.

## Table of Contents

1. [Installation](#Installation)
2. [Quick Start](#Quick-Start)
3. [Authentication](#authentication)
4. [Events and Report](#Events-and-Report)
5. [Campaigns](#Campaigns)
6. [Contacts](#Contacts)
7. [Messaging](#Messaging)
8. [Number](#Number)
9. [Phonebook](#Phonebook)
10. [SenderID](#SenderID)
11. [Templates](#Templates)
12. [Token](#Token)
13. [Contributing](#Contributing)
14. [License](#License)

## Installation

You can install the `termii_sdk` using `pip`:

```bash
pip install termii_sdk
```

## Quick Start

```python
from termii_sdk import TermiiSDK
from termii_sdk.core import Request

# Default sdk termii_enpoint
# TERMII_ENDPOINT = "https://api.ng.termii.com/api"

Request.termii_endpoint = 'your termii endpoint'

# Initialize the SDK with your API key
api_key = "your_api_key_here"
termii = TermiiSDK(api_key)

# Send an SMS message
message = "Hello from Termii SDK!"
phone_number = "+1234567890"
sender_id = "Test"
response = termii.send_message(to=phone_number, sms=message, from_=sender_id)
print("Message ID:", response.get("message_id"))
```

## Authentication

To use the Termii SDK, you need to provide your Termii API key when initializing the SDK. You can obtain your API key from your Termii account dashboard.

```python
from termii_sdk import *

api_key = "your_api_key_here"
termii = TermiiSDK(api_key)

```

## Events and Report

```python
response: Union[Error, BalanceResponse] = termii.balance()

response: Union[Error, SearchResponse] = termii.search()

response: Union[Error, StatusResponse] = termii.status()

response: Union[Error, HistoryResponse] = termii.history()

```

## Campaigns
```python
response: Union[Error, Response] = termii.send_campaign(
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
    )

response: Union[Error, FetchCampaignsResponse] = termii.fetch_campaigns()

response: Union[Error, FetchCampaignsHistoryResponse] = termii.fetch_campaign_history(campaign_id: str)

```

## Contacts
```python
response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_contacts(phonebook_id: str)

response: Union[Error, AddContactResponse]: = termii.add_contact(
        phonebook_id: str,
        phone_number: str,
        email_address: str,
        first_name: str,
        last_name: str,
        company: str,
        country_code: str,
    )

response: Union[Error, Response]: = termii.add_contacts(
        phonebook_id: str,
        contact_file: str,
        country_code: str,
    )

response: Union[Error, Response]: = termii.delete_contact_phonebook(contact_id: str)
```

## Messaging
```python

response: Union[Error, BasicResponse]: = termii.send_message(
        to: str,
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
        type: MediaType = MediaType.PLAIN,
        media_url: str = "",
        media_caption: str = "",
    )

response: Union[Error, BasicResponse]: = termii.send_bulk_message(
        to: list[str],
        from_: str,
        channel: Channel = Channel.GENERIC,
        sms: str = "",
    )
```

## Number
```python
response: Union[Error, BasicResponse]: = termii.send_message_number(
        to: str,
        sms: str = "",
    )
```

## Phonebook
```python
response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_phonebooks()

response: Union[Error, Response]: = termii.create_phonebook(
        phonebook_name: str,
        description: str,
    )

response: Union[Error, Response]: = termii.update_phonebook(
        phonebook_id: str,
        phonebook_name: str,
        description: str,
    )

response: Union[Error, Response]: = termii.delete_phonebook(phonebook_id: str)
```

## SenderID
```python
response: Union[Error, FetchSenderIDResponse]: = termii.fetch_id()

response: Union[Error, Response]: = termii.request_id(
        sender_id: str,
        usecase: str,
        company: str,
    )
```

## Templates
```python
response: Union[Error, BasicResponse]: = termii.device_template(
        phone_number: str,
        device_id: str,
        template_id: str,
        data: dict = None,
    )
```

## Token
```python
response: Union[Error, SendTokenResponse]: = termii.send_token(
        message_type: MessageType,
        to: str,
        from_: str,
        channel: Channel,
        pin_attempts: int,
        pin_time_to_live: int,
        pin_length: int,
        pin_placeholder: str,
        message_text: str,
        pin_type: MessageType,
    )

response: Union[Error, VoiceTokenResponse]: = termii.voice_token(
        phone_number: str,
        pin_attempts: str,
        pin_time_to_live: str,
        pin_length: str,
    )

response: Union[Error, VoiceCallResponse]: = termii.voice_call(
        phone_number: str,
        code: int,
    )

response: Union[Error, InAppTokenResponse]: = termii.in_app_token(
        phone_number: str,
        pin_type: MessageType,
        pin_attempts: int,
        pin_time_to_live: int,
        pin_length: int,
    )

response: Union[Error, VerifyTokenResponse]: = termii.verify_token(
        pin_id: str,
        pin: str,
    )

response: Union[Error, EmailTokenResponse]: = termii.email_token(
        email_address: str,
        code: str,
        email_configuration_id: str,
    )
```

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please submit a pull request.

## License

This SDK is released under the [MIT License](LICENSE).

---

Feel free to customize this documentation according to your SDK's features and your personal writing style. Make sure to update the content with accurate details and examples specific to the functions and methods your SDK provides.