# src/hypermodern_python_ems/console.py
import textwrap

import click
import requests

from . import __version__


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


@click.command()
@click.version_option(version=__version__)
def main():
    """The hypermodern Python project."""
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


#things to add:
#Display a friendly error message when the API is not reachable.
#Add an option to select the Wikipedia edition for another language.
#If you feel adventurous: auto-detect the user’s preferred language edition, using locale.
