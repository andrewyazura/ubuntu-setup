import click

from ..utils import echo_completion_message, run_commands

APT_COMMANDS = [
    "sudo apt update",
    "sudo apt upgrade -y",
    "sudo apt autoremove --purge -y",
]


@click.command()
def apt_upgrade(**_) -> None:
    run_commands(APT_COMMANDS)

    echo_completion_message("apt upgrade completed!")
