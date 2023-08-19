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
response = termii.send_message(to=phone_number, sms=message)
print("Message ID:", response.get("message_id"))
```

## Authentication

To use the Termii SDK, you need to provide your Termii API key when initializing the SDK. You can obtain your API key from your Termii account dashboard.

```python
from termii_sdk import *

api_key = "your_api_key_here"
termii = TermiiSDK(api_key)

kwargs = {}
```

## Events and Report

```python
response: Union[Error, BalanceResponse] = termii.balance(**kwargs)

response: Union[Error, SearchResponse] = termii.search(**kwargs)

response: Union[Error, StatusResponse] = termii.status(**kwargs)

response: Union[Error, HistoryResponse] = termii.history(**kwargs)

```

## Campaigns
```python
response: Union[Error, Response] = termii.send_campaign(**kwargs)

response: Union[Error, FetchCampaignsResponse] = termii.fetch_campaigns(**kwargs)

response: Union[Error, FetchCampaignsHistoryResponse] = termii.fetch_campaign_history(**kwargs)

```

## Contacts
```python
response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_contacts(**kwargs)

response: Union[Error, AddContactResponse]: = termii.add_contact(**kwargs)

response: Union[Error, Response]: = termii.add_contacts(**kwargs)

response: Union[Error, Response]: = termii.delete_contact_phonebook(**kwargs)
```

## Messaging
```python

response: Union[Error, BasicResponse]: = termii.send_message(**kwargs)

response: Union[Error, BasicResponse]: = termii.send_bulk_message(**kwargs)
```

## Number
```python
response: Union[Error, BasicResponse]: = termii.send_message_number(**kwargs)
```

## Phonebook
```python
response: Union[Error, FetchPhonebooksResponse]: = termii.fetch_phonebooks(**kwargs)

response: Union[Error, Response]: = termii.create_phonebook(**kwargs)

response: Union[Error, Response]: = termii.update_phonebook(**kwargs)

response: Union[Error, Response]: = termii.delete_phonebook(**kwargs)
```

## SenderID
```python
response: Union[Error, FetchSenderIDResponse]: = termii.fetch_id(**kwargs)

response: Union[Error, Response]: = termii.request_id(**kwargs)
```

## Templates
```python
response: Union[Error, BasicResponse]: = termii.device_template(**kwargs)
```

## Token
```python
response: Union[Error, SendTokenResponse]: = termii.send_token(**kwargs)

response: Union[Error, VoiceTokenResponse]: = termii.voice_token(**kwargs)

response: Union[Error, VoiceCallResponse]: = termii.voice_call(**kwargs)

response: Union[Error, InAppTokenResponse]: = termii.in_app_token(**kwargs)

response: Union[Error, VerifyTokenResponse]: = termii.verify_token(**kwargs)

response: Union[Error, EmailTokenResponse]: = termii.email_token(**kwargs)
```

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please submit a pull request.

## License

This SDK is released under the [MIT License](LICENSE).

---

Feel free to customize this documentation according to your SDK's features and your personal writing style. Make sure to update the content with accurate details and examples specific to the functions and methods your SDK provides.