# Copyright 2017 David R. Bild
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License

from setuptools import setup, Extension

import os, shutil, sys

if sys.platform == 'win32':
    LIB_NAMES = ['libssl64MD', 'libcrypto64MD']
else:
    LIB_NAMES = ['ssl']

_sslpsk = Extension('sslpsk._sslpsk',
                    sources = ['sslpsk/_sslpsk.c'],
                    libraries = LIB_NAMES,
                    library_dirs = ['openssl/lib/VC/'],
                    include_dirs = ['openssl/include']
)

setup(
    name = 'sslpsk',
    version = '1.0.0',
    description = 'Adds TLS-PSK support to the Python ssl package',
    author = 'David R. Bild',
    author_email = 'david@davidbild.org',
    license="Apache 2.0",
    url = 'https://github.com/drbild/sslpsk',
    download_url = 'https://github.com/drbild/sslpsk/archive/1.0.0.tar.gz',
    keywords = ['ssl', 'tls', 'psk', 'tls-psk', 'preshared key'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft'
    ],
    packages = ['sslpsk', 'sslpsk.test'],
    ext_modules = [_sslpsk],
    include_package_data=True,
    package_data = {'libssl' : ['openssl/bin/libssl-1_1-x64.dll', 'openssl/bin/libcrypto-1_1-x64.dll']},
    test_suite = 'sslpsk.test',
    zip_safe = False
)
