#!/usr/bin/env python

from pathlib import Path

from plumbum import local, FG
from plumbum.commands.processes import ProcessExecutionError

static_library_template = """\

static_dict = {static_dict!r}

def get_static_file(path):
    if path in static_dict:
        return static_dict[path]
    raise FileNotFoundError(path)

"""

ignore = ['.DS_Store']


def clean_build_artifacts():
    rm = local['rm']
    try:
        _ = rm['-r', 'build', 'dist'] & FG
    except ProcessExecutionError:
        pass


def clean_static_path(path: Path):
    _path = str(path).split('static/')
    return _path[1]


def generate_static_library(source: Path, target: Path):
    static_dict = {}
    static_files = [s for s in source.glob('**/*.*')
                    if s.name not in ignore]
    for static_file in static_files:
        cleaned_path = clean_static_path(static_file)
        with open(str(static_file), 'r') as infile:
            static_dict[str(cleaned_path)] = infile.read().strip()

    with open(str(target), 'w') as outfile:
        outfile.write(static_library_template.format(static_dict=static_dict))


if __name__ == '__main__':
    clean_build_artifacts()
    generate_static_library(Path('src/theinternet/static'), Path('src/theinternet/frozen_static.py'))
    pyinstaller = local['pyinstaller']
    _ = pyinstaller['--onefile', 'app.spec'] & FG
