import click

from ..utils import echo_completion_message, run_command

git_name_option = click.option("--name", prompt="git name")
git_email_option = click.option("--email", prompt="git email")


@click.command()
@git_name_option
@git_email_option
def setup_git(name: str, email: str, **_) -> None:
    run_command(f'git config --global user.name "{name}"')
    run_command(f'git config --global user.email "{email}"')

    echo_completion_message("git setup completed!")
