#!/usr/bin/python3

from pathlib import Path, PurePath
import sys, traceback

CHEATSHEETS_DIR = PurePath.joinpath(Path.home(), '.cheats')
EXISTING_SHEETS = map(lambda file : str(file).split('/')[-1], \
    sorted(Path(CHEATSHEETS_DIR).glob('*')))

def inform_invalid_sheet(message):
    print(message, file=sys.stderr)
    print('The following are available:', file=sys.stderr)
    print('\n'.join(EXISTING_SHEETS), file=sys.stderr)
    exit(1)

def find_next_section_index(begin_index, lines):
    spliced = lines[begin_index:]

    for line in spliced:
        if len(line) > 0 and line[0] == '#':
            return begin_index + spliced.index(line)

    return len(lines)

if len(sys.argv) > 1:
    if sys.argv[1] in EXISTING_SHEETS:
        sheet = open(PurePath.joinpath(CHEATSHEETS_DIR, sys.argv[1]), 'r').read()

        try:
            if (sys.argv[2] == '--section') or (sys.argv[2] == "-S"):
                try:
                    section = '# ' + sys.argv[3].lower()
                    sheet_lines = [line.lower() for line in sheet.splitlines()]
                    begin_index = sheet_lines.index(section) + 1
                    end_index = find_next_section_index(begin_index, sheet_lines) - 1
                    
                    if len(sheet_lines[end_index]) == 0: end_index -= 1                    

                    sheet = '\n'.join(sheet.splitlines()[begin_index: end_index + 1])
                except IndexError:
                    traceback.print_exc()
                    print('Section flag provided without section argument', \
                        file=sys.stderr)
                    exit(1)
                except ValueError:
                    print('Section not found!', file=sys.stderr)
                    exit(1)
        except IndexError:
            pass

        print(sheet)
    else:
        inform_invalid_sheet('Invalid cheatsheet argument provided')
else:
    inform_invalid_sheet('No cheatsheet argument provided!')

