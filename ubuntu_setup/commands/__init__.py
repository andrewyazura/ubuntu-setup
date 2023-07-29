import click

from .apps import install_apps
from .git import setup_git
from .pyenv import install_pyenv
from .spotify import install_spotify
from .zsh import install_zsh


def add_commands(cli: click.Group):
    cli.add_command(install_apps)
    cli.add_command(setup_git)
    cli.add_command(install_pyenv)
    cli.add_command(install_spotify)
    cli.add_command(install_zsh)
