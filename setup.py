from setuptools import setup, find_packages

setup(name='bitlyapi',
        version='0.1dev',
        description='A thin wrapper for the bit.ly REST api',
        author='Lars Kellogg-Stedman',
        author_email='lars@oddbit.com',
        packages=['bitlyapi'],
        scripts=['scripts/bitly',]
        )
