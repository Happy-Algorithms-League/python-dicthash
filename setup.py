# encoding: utf8
from setuptools import setup

setup(
    name='dicthash',
    version='0.0.1',
    author='Jakob Jordan, Maximilian Schmidt',
    author_email='j.jordan@fz-juelich.de',
    description=('Conveniently generate portable md5 hashes from (arbitrarily nested) dictionaries.'),
    license='MIT',
    keywords='hashing hash',
    url='https://github.com/INM-6/python-dicthash',
    packages=['dicthash'],
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
