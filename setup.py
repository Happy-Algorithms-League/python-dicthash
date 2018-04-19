# encoding: utf8
from setuptools import setup

setup(
    name='dicthash',
    version='0.0.1',
    author='Jakob Jordan, Maximilian Schmidt',
    author_email='j.jordan@fz-juelich.de',
    description=('Generate portable md5 hashes from (arbitrarily nested) dictionaries.'),
    license='MIT',
    keywords='hashing hash',
    url='https://github.com/INM-6/python-dicthash',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*, !=3.4.*, <4',
    install_requires=['future'],
    packages=['dicthash'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
