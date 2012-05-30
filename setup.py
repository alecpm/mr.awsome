from setuptools import setup
import os

version = "0.10"

install_requires = [
    'setuptools',
    'boto >= 1.9b',
    'Fabric >= 0.9.0',
    'lazy']

try:
    import argparse
    argparse    # make pyflakes happy...
except ImportError:
    install_requires.append('argparse >= 1.1')

setup(
    version=version,
    description="A script allowing to setup Amazon EC2 instances through configuration files.",
    long_description=open("README.txt").read() + "\n\n" +
                     open(os.path.join("docs", "HISTORY.txt")).read(),
    name="mr.awsome",
    author='Florian Schulze',
    author_email='florian.schulze@gmx.net',
    url='http://github.com/fschulze/mr.awsome',
    include_package_data=True,
    zip_safe=False,
    packages=['mr'],
    namespace_packages=['mr'],
    install_requires=install_requires,
    entry_points="""
      [console_scripts]
      aws = mr.awsome:aws
      assh = mr.awsome:aws_ssh
    """,
)