import json

from nbformat import from_dict

from papermill_slack.message import evaluate_notebook
from tests.conftest import TESTDATA_DIR


def test_exception_is_passed_to_message():
    notebook = from_dict(json.load((TESTDATA_DIR / "out_exception.ipynb").open()))

    message = evaluate_notebook(notebook)

    assert "Exception" in message.blocks[0].text.text


def test_success_is_passed_to_message():
    notebook = from_dict(json.load((TESTDATA_DIR / "out_parametrized.ipynb").open()))

    message = evaluate_notebook(notebook)

    assert "parametrized.ipynb" in message.blocks[0].text.text
    assert "00:00:01" in message.blocks[0].text.text


def test_parameters_are_added_to_context():
    notebook = from_dict(json.load((TESTDATA_DIR / "out_parametrized.ipynb").open()))

    message = evaluate_notebook(notebook)
    assert "*a:* 3" == message.blocks[1].elements[0].text
