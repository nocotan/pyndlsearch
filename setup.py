import os

from distutils.core import setup

def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == "":
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

package_dir = "pyndlsearch"

packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join(fullsplit(dirpath)))

setup(
    name = 'pyndlsearch',
    version = '0.1',
    description = 'A Python Wrapper for NDL Search API.',
    keywords = 'api, ndl, search, wrapper',
    license = 'MIT License',
    author = 'nocotan',
    author_email = 'noconoco.lib@gmail.com',
    url = 'http://github.com/nocotan/pyndlsearch/',
    packages = packages,
)
