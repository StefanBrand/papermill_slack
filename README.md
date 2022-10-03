# papermill_slack

This Python package sends the outcome of `papermill`-executed notebooks to a Slack channel via [incoming webhooks](https://api.slack.com/messaging/webhooks). It can be both used as a [`papermill` engine](https://papermill.readthedocs.io/en/latest/extending-entry-points.html#developing-a-new-engine), and as a stand-alone CLI tool. Stand-alone usage can be useful in scenarios, where another engine is in use, or for batch execution on multiple notebooks.


## Example

![Screenshot of a Slack message sent by papermill_slack](docs/papermill_slack_screenshot.png)


## Features

- ❗/ ✅ Distinguish executions with exceptions and successful executions
- ⏲ For successful executions post duration
- 🎲 For successful executions post parameters


## Installation
```
pip install git+https://github.com/StefanBrand/papermill_slack.git
```


## Usage

For all use-cases the environment variable `PAPERMILL_SLACK_WEBHOOK_URL` must be set, i.e.

```
export PAPERMILL_SLACK_WEBHOOK_URL=https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```


### Usage as a `papermill` engine

```
papermill --engine slack_engine my_notebook.ipynb my_executed_notebook.ipynb
```


### Usage as a stand-alone CLI tool

```
papermill_slack my_executed_notebook.ipynb
```

Or piping from `stdout` to `stdin`:

```
papermill my_notebook.ipynb - | papermill_slack -
```


## Development

The project uses `black` for formatting, `flake8` for linting, `mypy` for static type checking and `pytest` for unit tests. A `.devcontainer` exists for quick on-boarding in VSCode.