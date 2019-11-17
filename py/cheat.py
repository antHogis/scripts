#!/usr/bin/python3

from pathlib import Path, PurePath

CHEATSHEETS_DIR = PurePath.joinpath(Path.home(), '.cheats')
EXISTING_SHEETS = map(lambda file : str(file).split('/')[-1], \
    sorted(Path(CHEATSHEETS_DIR).glob('*')))

def list_sheets(): print('\n'.join(EXISTING_SHEETS))

def run():
    list_sheets()

run()
