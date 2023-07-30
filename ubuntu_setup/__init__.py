import click

from .commands import add_commands


@click.group()
@click.option("-d", "--debug", is_flag=True, help="print commands without executing them")
@click.option("-x", "--exit-first", is_flag=True, help="exit on first error")
@click.pass_context
def cli(ctx: click.Context, debug: bool, exit_first: bool) -> None:
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug
    ctx.obj["EXIT_FIRST"] = exit_first

    if debug:
        click.secho("debug mode is on 🐛", bold=True, bg="red")


add_commands(cli)
