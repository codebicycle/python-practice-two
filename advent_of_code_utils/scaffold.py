"""Download Advent of Code input and create solution stub."""
from string import Template
import os
import sys

import click
import requests

from secret import COOKIE


YEAR_DEFAULT = 2017
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
DAY_TEMPLATE = os.path.join(HERE, 'day_template.py')
HEADERS = {
    'cookie': COOKIE,
    'host': 'adventofcode.com',
}
CONFIG = {
    'directory': 'advent_of_code_{year}',
    'input_filename': 'input{day}.txt',
    'solution_filename': 'day{day}.py',
    'test_filename': 'test_day{day}.py',
    'input_url': 'http://adventofcode.com/{year}/day/{day}/input',
    'day_url': 'http://adventofcode.com/{year}/day/{day}',
}

def make_config(day, year):
    config = CONFIG.copy()
    for key, value in CONFIG.items():
        if isinstance(value, str):
            config[key] = value.format(day=day, year=year)
    return config

def file_write(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'File {filepath} created.')


class File:
    def __init__(self, config):
        self.config = config
        self.filename = None
        self.url = None
        self.filepath = None

    def get_filepath(self):
        filepath = os.path.join(ROOT, self.config['directory'], self.filename)
        return filepath

    def http_request(self, url):
        response = requests.get(url, headers=HEADERS)
        if response.status_code != requests.codes.ok:
            raise ValueError(f'Bad status code ({response.status_code}) returned from {url}.')
        return response.text

    def exists(self):
        return os.path.isfile(self.filepath)


class InputFile(File):
    def __init__(self, config):
        super().__init__(config)
        self.filename = config['input_filename']
        self.filepath = self.get_filepath()
        self.url = config['input_url']

    def make(self):
        if self.exists():
            print(f'File {self.filepath} exists!')
            return
        content = self.http_request(self.url)
        file_write(self.filepath, content)


class SolutionFile(File):
    def __init__(self, config):
        super().__init__(config)
        self.filename = config['solution_filename']
        self.filepath = self.get_filepath()
        self.url = config['day_url']

    def make(self):
        if self.exists():
            print(f'File {self.filepath} exists!')
            return
        day_description = self._get_description()
        content = self._fill_template(day_description)
        file_write(self.filepath, content)

    def _fill_template(self, day_description):
        with open(DAY_TEMPLATE) as f:
            template_str = f.read()

        template = Template(template_str)
        filled = template.substitute(
            day_description=day_description,
            input_filename=self.config['input_filename']
        )
        return filled

    def _get_description(self):
        # TODO Implement method
        # content = self.http_request(self.url)
        day_description = ''
        return day_description


@click.command()
@click.option('-d', '--day', type=int, required=True)
@click.option('-y', '--year', default=YEAR_DEFAULT)
def cli(day, year):
    config = make_config(day, year)
    InputFile(config).make()
    SolutionFile(config).make()


if __name__ == '__main__':
    cli()
