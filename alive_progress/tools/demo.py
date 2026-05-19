import logging
import time
from typing import NamedTuple

from .sampling import OVERHEAD_SAMPLING
from .utils import toolkit
from .. import alive_bar
from ..styles import BARS
from ..utils.colors import BOLD, ORANGE_IT


class Case(NamedTuple):
    name: str = None
    count: int = None
    config: dict = None
    done: bool = None
    hooks: bool = None
    title: str = None


def title(text):
    print(f'=== {BOLD.color_code}{ORANGE_IT(text)} ===')


cases = [
    Case(title='Definite/unknown modes'),
    Case('Normal+total', 1000, dict(total=1000)),
    Case('Underflow+total', 800, dict(total=1200)),
    Case('Overflow+total', 1200, dict(total=800)),
    Case('Unknown', 1000, dict(total=0)),

    Case(title='Manual modes'),
    Case('Normal+total+manual', 1000, dict(total=1000, manual=True)),
    Case('Underflow+total+manual', 800, dict(total=1200, manual=True)),
    Case('Overflow+total+manual', 1200, dict(total=800, manual=True)),
    Case('Unknown+manual', 1000, dict(total=0, manual=True)),

    Case(title='Print and Logging hooks'),
    Case('Simultaneous', 1000, dict(total=1000), hooks=True),

    # title('Quantifying mode')  # soon, quantifying mode...
    # ('Calculating auto', 1000, dict(total=..., manual=False)),
    # ('Calculating manual', 1000, dict(total=..., manual=True)),

    Case(title='Display features'),
    Case('Styles', 1000, dict(total=1000, bar='halloween', spinner='loving'))
]
features = [dict(total=1000, bar=bar, spinner='loving') for bar in BARS]
cases += [Case(name.capitalize(), 1000, {**features[i % len(BARS)], **config}, done=True)
          for i, (name, config) in enumerate(OVERHEAD_SAMPLING, 1)]




if __name__ == '__main__':
    parser, run = toolkit('Demonstrates alive-progress, showcasing several common scenarios.')
    parser.add_argument('sleep', type=float, nargs='?', help='the sleep time (default=.003)')

    run(demo)
