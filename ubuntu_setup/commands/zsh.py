import click

from ..utils import run_commands

INSTALL_COMMANDS = [
    "sudo apt install -y zsh",
    (
        'sh -c "$(curl -fsSL '
        'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    ),
    (
        "git clone https://github.com/spaceship-prompt/spaceship-prompt.git "
        '"$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1'
    ),
    (
        'ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" '
        '"$ZSH_CUSTOM/themes/spaceship.zsh-theme"'
    ),
]


@click.command()
def install_zsh() -> None:
    run_commands(INSTALL_COMMANDS)

    click.secho("zsh setup completed!", bg="green")
