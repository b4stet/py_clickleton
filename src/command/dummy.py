import click
import json
from src.command.abstract import AbstractCommand


class DummyCommand(AbstractCommand):
    def get_commands(self):
        group = click.Group('dummy', context_settings=dict(terminal_width=120))

        group.add_command(click.Command(
            name='a_command', help='helper for the command',
            callback=self.a_command,
            params=[self.get_option_output()]
        ))

        group.add_command(click.Command(
            name='another_command', help='helper of command',
            callback=self.another_command,
            params=[
                self.get_option_output(),
                self.get_option_meow(),
            ]
        ))

        return group

    def a_command(self, output):
        data = []
        for i in range(0, 5):
            data.append({
                'index': i,
                'name': 'event {}'.format(i),
                'type': 'welcome, it\'s a "dummy" text',
            })
        self.print(output, data)

    def another_command(self, output, meows=None):
        # validate user inputs
        # process
        data = []
        for meow in meows:
            data.append({
                'type': 'meow',
                'value': meow,
            })

        # print result
        self.print(output, data)
