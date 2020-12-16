 #!/usr/bin/env python

import io
from os.path import exists

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = "0.1.0"

setup(
    name='django_datatables',
    version=__version__,
    author='Ian Jones',
    packages=[
        'django_datatables',
        'django_datatables.static',
        'django_datatables.static.datatables',
        'django_datatables.static.datatables.css',
        'django_datatables.static.datatables.js',
        'django_datatables.templates',
        'django_datatables.templates.datatables',
        'django_datatables.templates.datatables.filter_blocks',
        'django_datatables.templates.datatables.filter_rows',
        'django_datatables.templates.datatables.plugins',
        'django_datatables.templatetags',
    ],
    include_package_data=True,
    scripts=[],
    url='https://github.com/jonesim/django-datatables',
    license='MIT',
    description='Datatables support for Django.',
    long_description=io.open('README.rst', encoding='utf-8').read() if exists("README.rst") else "",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    # install_requires=[
    #     'Django >= 2.1,<3.2',
    # ],
    zip_safe=False,
)
