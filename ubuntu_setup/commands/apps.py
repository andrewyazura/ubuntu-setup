import glob
from os import path

import click

from ..utils import echo_completion_message, run_command

deb_files_option = click.option(
    "--deb-files",
    prompt="path to folder with .deb packages",
    type=click.Path(exists=True, file_okay=False),
)


@click.command()
@deb_files_option
def install_apps(deb_files: str, **_) -> None:
    files = glob.glob(path.join(deb_files, "**/*.deb"), recursive=True)

    for file in files:
        run_command(f"sudo apt install -y {file}")

    echo_completion_message("app install completed!")
