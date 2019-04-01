#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst', 'r') as f:
    readme = f.read()

install_requires = ["dnspython >= 1.12.0"]

setup(
    name='domcheck',
    version='1.1.4.zapier',
    description='Domain Ownership Checker',
    long_description=readme,
    author='Olivier Poitrey',
    author_email='rs@dailymotion.com',
    url='https://github.com/rs/domcheck',
    keywords=["domain", "validation", "verification", "check", "ownership", "dns", "txt", "cname", "meta"],
    packages=['domcheck'],
    package_dir={'domcheck': 'domcheck'},
    install_requires=install_requires,
    test_suite='test',
    tests_require=['flake8', 'nose'],
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Security',
    ]
)
