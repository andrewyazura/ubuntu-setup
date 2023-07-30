import click

from ..utils import echo_completion_message, run_commands

INSTALL_COMMANDS = [
    "sudo apt install -y zsh curl",
    (
        'sh -c "$(curl -fsSL '
        'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" '
        '"" --unattended'
    ),
    (
        "git clone https://github.com/spaceship-prompt/spaceship-prompt.git "
        '"$HOME/.oh-my-zsh/custom/themes/spaceship-prompt" --depth=1'
    ),
    (
        'ln -s "$HOME/.oh-my-zsh/custom/themes/spaceship-prompt/spaceship.zsh-theme" '
        '"$HOME/.oh-my-zsh/custom/themes/spaceship.zsh-theme"'
    ),
]


@click.command()
def install_zsh(**_) -> None:
    run_commands(INSTALL_COMMANDS)

    echo_completion_message("zsh setup completed!")
