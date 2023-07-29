import click

from .commands import add_commands


@click.group()
@click.option("--debug", is_flag=True, help="print commands without executing them")
@click.pass_context
def cli(ctx, debug) -> None:
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug

    if debug:
        click.secho("debug mode is on", bg="red")


add_commands(cli)
