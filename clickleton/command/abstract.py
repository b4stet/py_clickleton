from abc import ABCMeta, abstractmethod
import click
import json
import csv
import sys


class AbstractCommand():
    OUTPUT_JSON = 'json'
    OUTPUT_CSV = 'csv'
    OUTPUTS = [OUTPUT_JSON, OUTPUT_CSV]

    def __init__(self):
        pass

    @abstractmethod
    def get_commands(self):
        raise NotImplementedError('Method get_commands must be implemented on class {}'.format(type(self)))

    def _print_formatted(self, output: str, data: list):
        if len(data) == 0:
            return

        if output == self.OUTPUT_JSON:
            print(json.dumps(data))

        if output == self.OUTPUT_CSV:
            header = list(data[0].keys())
            writer = csv.DictWriter(sys.stdout, quoting=csv.QUOTE_NONNUMERIC, quotechar='"', fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    def _get_option_output(self):
        return click.Option(
            ['--output', '-o', 'output'],
            help='Format to output result. Default is json',
            default='json',
            type=click.Choice(self.OUTPUTS)
        )

    def _get_option_meow(self):
        return click.Option(
            ['--meow', '-m', 'meows'],
            help='An option that can be repeated',
            multiple=True,
            type=str
        )

    def _get_option_flag_prompt(self):
        return click.Option(
            ['--flag', '-f', 'flag'],
            is_flag=True,
            default=False,
            help='Prompt for something sensitive like password',
            callback=self._prompt_flag
        )

    def _prompt_flag(self, ctx, param, flag):
        if flag is True:
            text = click.prompt(
                text='Enter something',
                hide_input=True,
                confirmation_prompt=True
            )

            return text
