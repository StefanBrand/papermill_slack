import os
from pathlib import Path

import pytest
import requests_mock

TESTS_DIR = Path(__file__).parent
TESTDATA_DIR = TESTS_DIR / "test_data"


@pytest.fixture
def requests_mocker_with_prepared_env(
    monkeypatch, requests_mock
) -> requests_mock.Mocker:
    monkeypatch.setenv("PAPERMILL_SLACK_WEBHOOK_URL", "http://foobar.com")
    requests_mock.post(os.environ["PAPERMILL_SLACK_WEBHOOK_URL"])

    return requests_mock
