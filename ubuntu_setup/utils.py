import subprocess

import click

from typing import TypeVar

T = TypeVar("T", str, list[str])


@click.pass_context
def run_command(ctx, command: T) -> None:
    if ctx.obj["DEBUG"]:
        click.secho(command, bg="black", fg="green")
        return

    subprocess.run(command, shell=True, check=True)


def run_commands(commands: list[T]) -> None:
    for command in commands:
        run_command(command)
