import json

import click
import nbformat

from papermill_slack.api import send_message
from papermill_slack.message import evaluate_notebook


@click.command()
@click.argument("notebook", type=click.File("r"))
def notebook_outcome_to_slack(notebook):
    """Reads notebook that was processed with papermill and sends outcome to Slack."""
    parsed_notebook = json.load(notebook)
    notebook_node = nbformat.from_dict(parsed_notebook)

    return send_message(evaluate_notebook(notebook_node))
