import click

from .signal import install_signal
from .spotify import install_spotify
from .zsh import install_zsh

COMMANDS = [
    setup_git,
    install_zsh,
    install_pyenv,
    install_signal,
    install_spotify,
    install_apps,
]

def add_commands(cli: click.Group) -> None:
    cli.add_command(auto)

    for command in COMMANDS:
        cli.add_command(command)
