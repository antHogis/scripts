#!/usr/bin/python3

from pathlib import Path, PurePath
import sys

CHEATSHEETS_DIR = PurePath.joinpath(Path.home(), '.cheats')
EXISTING_SHEETS = map(lambda file : str(file).split('/')[-1], \
    sorted(Path(CHEATSHEETS_DIR).glob('*')))

def inform_invalid_sheet(message):
    print(message, file=sys.stderr)
    print('The following are available:', file=sys.stderr)
    print('\n'.join(EXISTING_SHEETS), file=sys.stderr)
    exit(1)

if len(sys.argv) > 1:
    if sys.argv[1] in EXISTING_SHEETS:
        sheet = open(PurePath.joinpath(CHEATSHEETS_DIR, sys.argv[1]), 'r').read()
        print(sheet)
    else:
        inform_invalid_sheet('Invalid cheatsheet argument provided')
else:
    inform_invalid_sheet('No cheatsheet argument provided!')

