import click

from ..utils import echo_completion_message, run_commands

INSTALL_COMMANDS = [
    (
        "curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | "
        "sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg"
    ),
    (
        'echo "deb http://repository.spotify.com stable non-free" | '
        "sudo tee /etc/apt/sources.list.d/spotify.list"
    ),
    "sudo apt update",
    "sudo apt install -y spotify-client",
]


@click.command()
def install_spotify(**_) -> None:
    run_commands(INSTALL_COMMANDS)

    echo_completion_message("spotify install completed!")
