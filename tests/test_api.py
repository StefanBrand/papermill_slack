from unittest import mock

import pytest

from papermill_slack.api import WebhookUrlNotSetException, send_message


def test_api_raises_exception_if_webhook_url_not_set():
    with pytest.raises(WebhookUrlNotSetException):
        send_message(mock.Mock())


def test_api_sends_slack_request(requests_mocker_with_prepared_env):
    mocked_message = mock.Mock()
    mocked_message.build.return_value = dict()

    send_message(mocked_message)

    assert requests_mocker_with_prepared_env.call_count == 1
