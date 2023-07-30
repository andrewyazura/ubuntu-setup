import click

from ..utils import echo_completion_message, run_commands

INSTALL_COMMANDS = [
    (
        "wget -O- https://updates.signal.org/desktop/apt/keys.asc | "
        "gpg --dearmor > signal-desktop-keyring.gpg"
    ),
    (
        "cat signal-desktop-keyring.gpg | "
        "sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null"
    ),
    (
        "echo 'deb "
        "[arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] "
        "https://updates.signal.org/desktop/apt xenial main' | "
        "sudo tee /etc/apt/sources.list.d/signal-xenial.list"
    ),
    "sudo apt update",
    "sudo apt install -y signal-desktop",
]


@click.command()
def install_signal(**_) -> None:
    run_commands(INSTALL_COMMANDS)

    echo_completion_message("signal desktop install completed!")
