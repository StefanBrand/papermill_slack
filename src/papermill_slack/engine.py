from papermill.engines import NBClientEngine
from requests import Response

from papermill_slack.api import send_message
from papermill_slack.message import evaluate_notebook


class WebhookUrlNotSetException(Exception):
    pass


class PapermillSlackEngine(NBClientEngine):
    @classmethod
    def execute_managed_notebook(cls, nb_man, kernel_name, **kwargs) -> Response:

        # call the papermill execution engine:
        super().execute_managed_notebook(nb_man, kernel_name, **kwargs)

        return send_message(evaluate_notebook(nb_man.nb))
