import subprocess

import click

from typing import TypeVar

T = TypeVar("T", str, list[str])


@click.pass_context
def run_command(ctx, command: T) -> None:
    if ctx.obj["DEBUG"]:
        click.secho(command, fg="red")
        return

    subprocess.run(command, shell=True, check=True)


def run_commands(commands: list[T]) -> None:
    for command in commands:
        run_command(command)


def echo_completion_message(message: str):
    click.secho(f"{message} ✅", bold=True, fg="green")
