import timeit

from about_time.human_duration import fn_human_duration

from .utils import toolkit
from ..core.configuration import config_handler
from ..core.progress import __alive_bar

human_duration = fn_human_duration(False)




OVERHEAD_SAMPLING_GROUP = [
    ('definite', dict(total=1)),
    ('manual(b)', dict(total=1, manual=True)),
    ('manual(u)', dict(manual=True)),
    ('unknown', dict()),
]
OVERHEAD_SAMPLING = [
    ('default', dict()),
    ('receipt', dict(receipt_text=True)),
    ('no spinner', dict(spinner=None)),
    ('no elapsed', dict(elapsed=False)),
    ('no monitor', dict(monitor=False)),
    ('no stats', dict(stats=False)),
    ('no bar', dict(bar=None)),
    ('only spinner', dict(bar=None, monitor=False, elapsed=False, stats=False)),
    ('only elapsed', dict(bar=None, spinner=None, monitor=False, stats=False)),
    ('only monitor', dict(bar=None, spinner=None, elapsed=False, stats=False)),
    ('only stats', dict(bar=None, spinner=None, monitor=False, elapsed=False)),
    ('only bar', dict(spinner=None, monitor=False, elapsed=False, stats=False)),
    ('none', dict(bar=None, spinner=None, monitor=False, elapsed=False, stats=False)),
]






class __lock:
    def __enter__(self):
        pass

    def __exit__(self, _type, value, traceback):
        pass


if __name__ == '__main__':
    parser, run = toolkit('Estimates the alive_progress overhead per cycle on your system.')

    run(overhead_sampling)
