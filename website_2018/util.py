from pkgutil import walk_packages
from importlib import import_module
from pathlib import Path
import logging
import scss
import glob
import os

log = logging.getLogger(__name__)


def import_subpackages(name, path, env):
    """
        Imports all subpackages of the module defined by
        name and path into the provided env.
        eg. import_subpackages(__name__, __path__, globals())
        Returns list of all imported modules
    """
    log.info(f"Importing all sub-packages of {name}.")
    _all = []
    for _, pkg_name, _ in walk_packages(path):
        fullname = f"{name}.{pkg_name}"
        log.info(fullname)
        imported = import_module(fullname)
        env[pkg_name] = imported
        _all.append((pkg_name, fullname, imported))
    return _all


def compile_scss(basedir, infile, outfile):
    compiled = scss.compiler.compile_file(Path(infile),)
    with open(outfile, 'w') as o:
        o.write(compiled)
