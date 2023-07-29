import click

from ..utils import run_command


@click.command()
@click.option("--name", prompt="git name")
@click.option("--email", prompt="git email")
def setup_git(name, email) -> None:
    run_command(f'git config --global user.name "{name}"')
    run_command(f'git config --global user.email "{email}"')

    click.secho("git setup completed!", bg="green")
