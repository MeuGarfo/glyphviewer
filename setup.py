#!/usr/bin/env python

from setuptools import setup

setup(name='glyphviewer',
    version='0.6',
    description='A Django app for examining web fonts and the characters they contain.',
    author='Peter Murphy',
    author_email='peterkmurphy@gmail.com',
    url='http://pypi.python.org/pypi/glyphviewer/',
    packages=['glyphviewer', 'glyphviewer.templatetags'],
    package_data={
        'glyphviewer': [
            'templates/glyphviewer/*.html',
            'static/glyphviewer/fonts/*.woff',
        ],
    },
    keywords = 'font glyph web woff ttf otf TrueType OpenType Django',
    license='LICENSE.txt',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Topic :: Artistic Software',
        'Topic :: Education',
        'Topic :: System :: Console Fonts',
        'Topic :: Text Processing :: Fonts',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
        ],
    long_description=open('README.rst').read(),
    install_requires = ["Django >= 1.0", "fonttools >= 3.0", "numpy >= 1.0", "brotli"],
)
