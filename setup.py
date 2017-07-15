from codecs import open
from os import path
import setuptools

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='factor_rotation',

    version='0.1.0',

    description='Factor rotation algorithms',
    long_description=long_description,
    url='https://github.com/mvds314/factor_rotation',
    author='Martin van der Schans',
    license='BSD',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='factorization pca factor-analysis rotation',
    packages=['factor_rotation'],
    install_requires=[
        'numpy',
        'scipy',
    ]
)
