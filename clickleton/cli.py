import click
from clickleton.command.dummy import DummyCommand


cli = click.Group('cli')
cli.add_command(DummyCommand().get_commands())

if __name__ == '__main__':
    cli()
