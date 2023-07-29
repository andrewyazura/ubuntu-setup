import glob
from os import path

import click

from ..apps.docker_desktop import install_docker_desktop
from ..utils import run_command


@click.command()
@click.option(
    "--deb-files",
    prompt="path to folder with .deb packages",
    type=click.Path(exists=True, file_okay=False),
)
def install_apps(deb_files) -> None:
    files = glob.glob(path.join(deb_files, "**/*.deb"), recursive=True)

    for file in files:
        if "docker" in file.lower() and "desktop" in file.lower():
            install_docker_desktop(file)
            continue

        run_command(f"sudo apt install -y {file}")

    click.secho("app install completed!", bg="green")
