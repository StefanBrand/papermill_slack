import os

import requests
from blockkit import Message
from requests import Response


class WebhookUrlNotSetException(Exception):
    pass


def send_message(message: Message) -> Response:
    try:
        webhook_url = os.environ["PAPERMILL_SLACK_WEBHOOK_URL"]
    except KeyError as e:
        raise WebhookUrlNotSetException(
            "The environment variable PAPERMILL_SLACK_WEBHOOK_URL must be set."
        ) from e

    return requests.post(webhook_url, json=message.build())
