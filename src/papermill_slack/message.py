from datetime import datetime
from enum import Enum
from pathlib import Path

from blockkit import Context, Message, Section
from nbformat import NotebookNode


class Emoji(Enum):
    SUCCESS = "white_check_mark"
    FAILURE = "exclamation"


def generate_blockkit_message(
    message: str, emoji: Emoji, extra_context: dict = dict()
) -> Message:
    blocks = [Section(text=f":{emoji.value}: {message}")]

    if extra_context:
        blocks.append(
            Context(
                elements=[f"*{name}:* {value}" for name, value in extra_context.items()]
            )
        )

    return Message(blocks=blocks)


def evaluate_notebook(notebook: NotebookNode) -> Message:
    context = notebook.metadata.papermill.parameters

    if notebook.metadata.papermill.exception:
        exception_cell = next(
            filter(
                lambda cell: cell.metadata.get("papermill")
                and cell.metadata.papermill.exception,
                notebook.cells,
            )
        )

        error_output = next(
            filter(
                lambda output: output["output_type"] == "error", exception_cell.outputs
            )
        )

        return generate_blockkit_message(
            f"{error_output['ename']}: {error_output['evalue']}",
            emoji=Emoji.FAILURE,
            extra_context=context,
        )

    else:
        # NOTE: duration only exists after engine has called notebook_complete
        duration = (
            notebook.metadata.papermill.duration
            or (
                datetime.now()
                - datetime.fromisoformat(notebook.metadata.papermill.start_time)
            ).total_seconds()
        )
        duration_string = datetime.fromtimestamp(duration).strftime("%H:%M:%S")

        return generate_blockkit_message(
            f"{Path(notebook.metadata.papermill.input_path).name} "
            f"finished successfully after {duration_string}",
            emoji=Emoji.SUCCESS,
            extra_context=context,
        )
