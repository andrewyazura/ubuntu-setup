import click

from ..utils import echo_completion_message
from .apps import deb_files_option, install_apps
from .apt import apt_upgrade
from .git import git_email_option, git_name_option, setup_git
from .pyenv import install_pyenv, pyenv_shell_option
from .signal import install_signal
from .spotify import install_spotify
from .zsh import install_zsh

COMMANDS = [
    apt_upgrade,
    setup_git,
    install_zsh,
    install_pyenv,
    install_signal,
    install_spotify,
    install_apps,
]


@click.command(context_settings=dict(ignore_unknown_options=True))
@git_name_option
@git_email_option
@pyenv_shell_option
@deb_files_option
@click.pass_context
def run(ctx: click.Context, **_) -> None:
    for command in COMMANDS:
        ctx.forward(command)

    echo_completion_message("auto setup completed!")


def add_commands(cli: click.Group) -> None:
    cli.add_command(run)

    for command in COMMANDS:
        cli.add_command(command)
