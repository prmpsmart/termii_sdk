"""Constants used in the library
__author_github__ = https://github.com/prmpsmart
__author__ = prmpsmart@gmail.com
"""


from .core import (
    BasicResponse,
    Response,
    Json,
    Request,
    RequestType,
    Channel,
    MessageType,
)


# -----------------------------------
# Enum classes


# -----------------------------------
# Data classes


class InAppTokenData:
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.pin_id: str = json.pin_id
        self.otp: int = json.otp
        self.phone_number: int = json.phone_number
        self.phone_number_other: str = json.phone_number_other


# -----------------------------------
# Responses classes
class SendTokenResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.pinId: str = json.pinId
        self.to: str = json.to
        self.smsStatus: str = json.smsStatus


class VoiceTokenResponse(BasicResponse):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.pinId: str = json.pinId


class VoiceCallResponse(VoiceTokenResponse):
    ...


class InAppTokenResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.status: str = json.status
        self.to: str = json.to
        self.smsStatus: str = json.smsStatus


class VerifyTokenResponse(Response):
    def __init__(self, json: Json) -> None:
        super().__init__(json)

        self.pinId: str = json.pinId
        self.verified: str = json.verified
        self.msisdn: str = json.msisdn


class EmailTokenResponse(BasicResponse):
    ...


# -----------------------------------
# Request classes


class Token(Request):
    """Token allows businesses generate, send and verify one-time-passwords.
    The Token API is organised around using HTTP verbs and REST. Our API accepts and returns JSON formatted payload.
    """

    endpoint = "sms/otp"

    def __init__(self, api_key: str) -> None:
        super().__init__(api_key)

    def send_token(
        self,
        *,
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
    ) -> SendTokenResponse:
        """The send token API allows businesses trigger one-time-passwords (OTP) across any available messaging channel on Termii. One-time-passwords created are generated randomly and there's an option to set an expiry time."""

        json = Json(
            message_type=message_type.value,
            to=to,
            channel=channel.value,
            pin_attempts=pin_attempts,
            pin_time_to_live=pin_time_to_live,
            pin_length=pin_length,
            pin_placeholder=pin_placeholder,
            message_text=message_text,
            pin_type=pin_type.value,
        )
        json["from"] = from_

        return self.make_request(
            requests_type=RequestType.POST,
            path="send",
            json=json,
            response_class=SendTokenResponse,
        )

    def voice_token(
        self,
        *,
        phone_number: str,
        pin_attempts: str,
        pin_time_to_live: str,
        pin_length: str,
    ) -> VoiceTokenResponse:
        """The voice token API enables you to generate and trigger one-time passwords (OTP) through the voice channel to a phone number. OTPs are generated and sent to the phone number and can only be verified using our Verify Token API ."""

        json = Json(
            phone_number=phone_number,
            pin_attempts=pin_attempts,
            pin_time_to_live=pin_time_to_live,
            pin_length=pin_length,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            path="send/voice",
            json=json,
            response_class=VoiceTokenResponse,
        )

    def voice_call(
        self,
        *,
        phone_number: str,
        code: int,
    ) -> VoiceCallResponse:
        """The voice call API enables you to send messages from your application through our voice channel to a phone number. Only one-time-passwords (OTP) are allowed for now and these OTPs can not be verified using our Verify Token API."""

        json = Json(
            phone_number=phone_number,
            code=code,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            path="call",
            json=json,
            response_class=VoiceCallResponse,
        )

    def in_app_token(
        self,
        *,
        phone_number: str,
        pin_type: MessageType,
        pin_attempts: int,
        pin_time_to_live: int,
        pin_length: int,
    ) -> InAppTokenResponse:
        """This API returns OTP codes in JSON format which can be used within any web or mobile app. Tokens are numeric or alpha-numeric codes generated to authenticate login requests and verify customer transactions."""

        json = Json(
            phone_number=phone_number,
            pin_type=pin_type.value,
            pin_attempts=pin_attempts,
            pin_time_to_live=pin_time_to_live,
            pin_length=pin_length,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            path="generate",
            json=json,
            response_class=InAppTokenResponse,
        )

    def verify_token(
        self,
        *,
        pin_id: str,
        pin: str,
    ) -> VerifyTokenResponse:
        """Verify token API, checks tokens sent to customers and returns a response confirming the status of the token. A token can either be confirmed as verified or expired based on the timer set for the token."""
        json = Json(
            pin_id=pin_id,
            pin=pin,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            path="verify",
            json=json,
            response_class=VerifyTokenResponse,
        )

    def email_token(
        self,
        *,
        email_address: str,
        code: str,
        email_configuration_id: str,
    ):
        """The email token API enables you to send one-time-passwords from your application through our email channel to an email address. Only one-time-passwords (OTP) are allowed for now and these OTPs can not be verified using our Verify Token API."""

        json = Json(
            email_address=email_address,
            code=code,
            email_configuration_id=email_configuration_id,
        )

        return self.make_request(
            requests_type=RequestType.POST,
            endpoint="email/otp/send",
            json=json,
            response_class=EmailTokenResponse,
        )
