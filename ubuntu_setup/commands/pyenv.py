import click

from ..utils import run_commands

INSTALL_COMMANDS = [
    "curl https://pyenv.run | bash",
    (
        "sudo apt install -y build-essential libssl-dev zlib1g-dev "
        "libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev "
        "xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev"
    ),
]

ZSH_SETUP = [
    "echo 'export PYENV_ROOT=\"$HOME/.pyenv\"' >> ~/.zshrc",
    (
        "echo 'command -v pyenv >/dev/null || "
        'export PATH="$PYENV_ROOT/bin:$PATH"\' >> ~/.zshrc'
    ),
    "echo 'eval \"$(pyenv init -)\"' >> ~/.zshrc",
]

BASH_SETUP = [
    "echo 'export PYENV_ROOT=\"$HOME/.pyenv\"' >> ~/.bashrc",
    (
        "echo 'command -v pyenv >/dev/null || "
        'export PATH="$PYENV_ROOT/bin:$PATH"\' >> ~/.bashrc'
    ),
    "echo 'eval \"$(pyenv init -)\"' >> ~/.bashrc",
]


@click.command()
@click.option(
    "--shell",
    default="other",
    type=click.Choice(["zsh", "bash", "other"], case_sensitive=False),
)
def install_pyenv(shell: str) -> None:
    run_commands(INSTALL_COMMANDS)

    match shell:
        case "zsh":
            run_commands(ZSH_SETUP)

        case "bash":
            run_commands(BASH_SETUP)

        case _:
            click.echo(
                "unknown shell env, read the docs: "
                "https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv"
            )

    click.secho("pyenv setup completed!", bg="green")
