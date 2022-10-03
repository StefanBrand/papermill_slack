import pytest
from click.testing import CliRunner

from papermill_slack.cli import notebook_outcome_to_slack
from tests.conftest import TESTDATA_DIR


@pytest.mark.usefixtures("requests_mocker_with_prepared_env")
def test_cli():
    runner = CliRunner()
    result = runner.invoke(
        notebook_outcome_to_slack, [str(TESTDATA_DIR / "out_parametrized.ipynb")]
    )

    assert result.exit_code == 0
