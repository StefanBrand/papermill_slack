from unittest import mock

import papermill as pm
import pytest

from tests.conftest import TESTDATA_DIR

NOTEBOOK_FILE = "out_parametrized.ipynb"


# do not actually execute notebook
@mock.patch("papermill.engines.NBClientEngine.execute_managed_notebook", mock.Mock())
@pytest.mark.usefixtures("requests_mocker_with_prepared_env")
def test_engine_sends_slack_request(tmp_path):
    result_notebook = pm.execute_notebook(
        TESTDATA_DIR / NOTEBOOK_FILE,
        tmp_path / NOTEBOOK_FILE,
        engine_name="slack_engine",
    )

    assert "papermill" in result_notebook.metadata
