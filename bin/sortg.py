#!/usr/bin/env python
# Sorts the glossary alphabetically

import os
import shutil
import argparse

from operator import itemgetter
from collections import defaultdict


BASEDIR = os.path.join(os.path.dirname(__file__), "..")
GLOSSARY = os.path.normpath(os.path.join(BASEDIR, "GLOSSARY.md"))


def sort_glossary(path=GLOSSARY, backup=True):
    """
    Modifies the glossary file in place by loading the data into memory,
    sorting it, then rewriting it back to the file. If backup is specified,
    it will make an ".orig" version of the file before overwriting.
    """
    if backup:
        dst = path + ".orig"
        shutil.copy(path, dst)
        print("made backup of {} at {}".format(path, dst))

    terms = defaultdict(str)

    with open(path, 'r') as f:
        current = None

        for line in f:
            if line.startswith("##"):
                current = line
                continue

            else:
                if current is None: continue
                terms[current] += line

    with open(path, 'w') as f:
        for term, definition in sorted(terms.items(), key=itemgetter(0)):
            f.write(term)
            f.write(definition)

    print("{} has had {} terms sorted".format(path, len(terms)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Sorts the glossary alphabetically."
    )

    parser.add_argument(
        '-b', '--backup', action='store_true', default=False,
        help='create a .orig file from the original as backup',
    )

    parser.add_argument(
        'glossary', default=GLOSSARY, nargs="?", type=str,
        help='path to the glossary file if different from GitBook default',
    )

    args = parser.parse_args()
    sort_glossary(args.glossary, args.backup)
