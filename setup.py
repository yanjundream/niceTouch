#!/usr/bin/env python3

"""
    Easily configure multiple touch and non touch screens on a single linux system.
    Copyright (C) 2017  Kevin Sandom

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

setup(
        name = 'niceTouch',
        version = '2019.2.10.1',
        scripts = ['nt'],
        packages = ['niceTouch'],
        install_requires = ['PyYAML'],
        url = 'https://github.com/ksandom/niceTouch',
        author = 'Kevin Sandom',
        author_email = 'kjsandom@gmail.com'
    )
