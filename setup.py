import io
import re

from os.path import (
    dirname,
    join,
)
from setuptools import setup, find_packages


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='theinternet',
    version='0.1',
    license='BSD License',
    description='',
    long_description='%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst'))),
    author='Harshad Sharma',
    author_email='harshad@sharma.io',
    url='https://github.com/hiway/theinternet.lol',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        'quart',
        'makeweb',
        'atum',
    ],
    dev_requires=[
        'plumbum',
        'pyinstaller',
    ],
    entry_points='''
    [console_scripts]
    theinternet=theinternet.cli:main
    ''',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
