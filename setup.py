from setuptools import setup, find_packages

setup(
    name="papermill_slack",
    version="0.1",
    url="https://github.com/StefanBrand/papermill_slack",
    author="Stefan Brand",
    author_email="stefan.brands@eox.at",
    description="A papermill engine that posts success/failure "
    "of notebook execution to Slack.",
    packages=find_packages("./src"),
    package_dir={"": "src"},
    install_requires=["blockkit", "click", "nbformat", "papermill", "requests"],
    entry_points={
        "papermill.engine": [
            "slack_engine=papermill_slack.engine:PapermillSlackEngine"
        ],
        "console_scripts": [
            "papermill_slack = papermill_slack.cli:notebook_outcome_to_slack",
        ],
    },
)
