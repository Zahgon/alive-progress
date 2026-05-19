import os.path
import urllib.request
from itertools import zip_longest

from .utils import toolkit
from ..utils.cells import split_graphemes
from ..utils.colors import GREEN, ORANGE, RED

CACHE = '.unicode_cache'




def find_groups(data, max_diff):
    """Group some numbers with a maximum difference between them.
    I've used to try to fix the current grapheme break error.

    Using version unicode 13.1:
        Component
          - skin-tone
         🏻    XX: 1 != 2 -> |1f3fb 1f3fb|-| c light
         🏻   aXa: 2 != 3 -> |61 1f3fb|61|-| c light
         🏻   aaX: 2 != 3 -> |61|61 1f3fb|-| c light
         🏼    XX: 1 != 2 -> |1f3fc 1f3fc|-| c medium-light
         🏼   aXa: 2 != 3 -> |61 1f3fc|61|-| c medium-light
         🏼   aaX: 2 != 3 -> |61|61 1f3fc|-| c medium-light
         🏽    XX: 1 != 2 -> |1f3fd 1f3fd|-| c medium
         🏽   aXa: 2 != 3 -> |61 1f3fd|61|-| c medium
         🏽   aaX: 2 != 3 -> |61|61 1f3fd|-| c medium
         🏾    XX: 1 != 2 -> |1f3fe 1f3fe|-| c medium-dark
         🏾   aXa: 2 != 3 -> |61 1f3fe|61|-| c medium-dark
         🏾   aaX: 2 != 3 -> |61|61 1f3fe|-| c medium-dark
         🏿    XX: 1 != 2 -> |1f3ff 1f3ff|-| c dark
         🏿   aXa: 2 != 3 -> |61 1f3ff|61|-| c dark
         🏿   aaX: 2 != 3 -> |61|61 1f3ff|-| c dark

    The codepoints that do accept a skin tone are:
    0x0261D, 0x026F9, 0x0270A, 0x0270B, 0x0270C, 0x0270D, 0x1F385, 0x1F3C2, 0x1F3C3, 0x1F3C4,
    0x1F3C7, 0x1F3CA, 0x1F3CB, 0x1F3CC, 0x1F442, 0x1F443, 0x1F446, 0x1F447, 0x1F448, 0x1F449,
    0x1F44A, 0x1F44B, 0x1F44C, 0x1F44D, 0x1F44E, 0x1F44F, 0x1F450, 0x1F466, 0x1F467, 0x1F468,
    0x1F469, 0x1F46B, 0x1F46C, 0x1F46D, 0x1F46E, 0x1F470, 0x1F471, 0x1F472, 0x1F473, 0x1F474,
    0x1F475, 0x1F476, 0x1F477, 0x1F478, 0x1F47C, 0x1F481, 0x1F482, 0x1F483, 0x1F485, 0x1F486,
    0x1F487, 0x1F4AA, 0x1F574, 0x1F575, 0x1F57A, 0x1F590, 0x1F595, 0x1F596, 0x1F645, 0x1F646,
    0x1F647, 0x1F64B, 0x1F64C, 0x1F64D, 0x1F64E, 0x1F64F, 0x1F6A3, 0x1F6B4, 0x1F6B5, 0x1F6B6,
    0x1F6C0, 0x1F6CC, 0x1F90C, 0x1F90F, 0x1F918, 0x1F919, 0x1F91A, 0x1F91B, 0x1F91C, 0x1F91E,
    0x1F91F, 0x1F926, 0x1F930, 0x1F931, 0x1F932, 0x1F933, 0x1F934, 0x1F935, 0x1F936, 0x1F937,
    0x1F938, 0x1F939, 0x1F93D, 0x1F93E, 0x1F977, 0x1F9B5, 0x1F9B6, 0x1F9B8, 0x1F9B9, 0x1F9BB,
    0x1F9CD, 0x1F9CE, 0x1F9CF, 0x1F9D1, 0x1F9D2, 0x1F9D3, 0x1F9D4, 0x1F9D5, 0x1F9D6, 0x1F9D7,
    0x1F9D8, 0x1F9D9, 0x1F9DA, 0x1F9DB, 0x1F9DC, 0x1F9DD

    """
    pass


if __name__ == '__main__':
    parser, run = toolkit('Tests the grapheme break implementation against some unicode version.')
    parser.add_argument('uver', type=float, nargs='?', help='the unicode version to be used')
    parser.add_argument('--all', dest='show_all', action='store_true',
                        help='shows the correct cases, in addition to the wrong ones')
    parser.add_argument('--no-cache', dest='cache', action='store_false',
                        help='ignores the cache and re-downloads the spec')

    run(validate_unicode_breaks)
